# ONLINE LEARNING MANAGEMENT SYSTEM

import os
from datetime import datetime


# BASE CLASS


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display(self):
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")



# INHERITANCE


class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.enrolled_courses = {}

    def display(self):
        print("\n--- Student Details ---")
        super().display()
        print("Enrolled Courses:", len(self.enrolled_courses))


class Instructor(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.created_courses = []

    def display(self):
        print("\n--- Instructor Details ---")
        super().display()
        print("Courses Created:", len(self.created_courses))



# COURSE CLASS


class Course:
    def __init__(self, course_id, title, instructor_id):
        self.course_id = course_id
        self.title = title
        self.instructor_id = instructor_id

        # Nested dictionary for learning modules
        self.modules = {}

        # Assignment details
        self.assignments = {}

    def add_module(self, module_id, module_name):
        self.modules[module_id] = {
            "name": module_name,
            "completed_students": []
        }

    def add_assignment(self, assignment_id, assignment_name, max_score):
        self.assignments[assignment_id] = {
            "name": assignment_name,
            "max_score": max_score,
            "scores": {}
        }

    def display(self):
        print("\n================================")
        print("Course ID:", self.course_id)
        print("Course Name:", self.title)
        print("Instructor ID:", self.instructor_id)

        print("\nLearning Modules:")
        if self.modules:
            for module_id, module in self.modules.items():
                print(module_id, "-", module["name"])
        else:
            print("No modules available.")

        print("\nAssignments:")
        if self.assignments:
            for assignment_id, assignment in self.assignments.items():
                print(
                    assignment_id,
                    "-",
                    assignment["name"],
                    "(Max Score:",
                    assignment["max_score"],
                    ")"
                )
        else:
            print("No assignments available.")



# LMS CLASS


class LMS:

    def __init__(self):
        self.students = {}
        self.instructors = {}
        self.courses = {}

        # Nested dictionary
        # student_id -> course_id -> progress information
        self.enrollments = {}

        self.load_data()

    
    # STUDENT REGISTRATION
    

    def register_student(self):
        try:
            student_id = input("Enter Student ID: ").strip()

            if student_id in self.students:
                raise ValueError("Student ID already exists.")

            name = input("Enter Student Name: ").strip()
            email = input("Enter Email: ").strip()

            if not name or not email:
                raise ValueError("Name and email cannot be empty.")

            student = Student(student_id, name, email)

            self.students[student_id] = student
            self.enrollments[student_id] = {}

            print("Student registered successfully.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # INSTRUCTOR REGISTRATION
    

    def register_instructor(self):
        try:
            instructor_id = input("Enter Instructor ID: ").strip()

            if instructor_id in self.instructors:
                raise ValueError("Instructor ID already exists.")

            name = input("Enter Instructor Name: ").strip()
            email = input("Enter Email: ").strip()

            if not name or not email:
                raise ValueError("Name and email cannot be empty.")

            instructor = Instructor(
                instructor_id,
                name,
                email
            )

            self.instructors[instructor_id] = instructor

            print("Instructor registered successfully.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # COURSE CREATION
    

    def create_course(self):
        try:
            instructor_id = input("Enter Instructor ID: ").strip()

            if instructor_id not in self.instructors:
                raise ValueError("Instructor does not exist.")

            course_id = input("Enter Course ID: ").strip()

            if course_id in self.courses:
                raise ValueError("Course ID already exists.")

            title = input("Enter Course Name: ").strip()

            if not title:
                raise ValueError("Course name cannot be empty.")

            course = Course(
                course_id,
                title,
                instructor_id
            )

            self.courses[course_id] = course

            self.instructors[instructor_id].created_courses.append(course_id)

            print("Course created successfully.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # COURSE ENROLLMENT
    

    def enroll_student(self):
        try:
            student_id = input("Enter Student ID: ").strip()

            if student_id not in self.students:
                raise ValueError("Student does not exist.")

            course_id = input("Enter Course ID: ").strip()

            if course_id not in self.courses:
                raise ValueError("Course does not exist.")

            if course_id in self.enrollments[student_id]:
                raise ValueError("Student is already enrolled.")

            self.enrollments[student_id][course_id] = {
                "completed_modules": [],
                "scores": {},
                "completion": 0
            }

            self.students[student_id].enrolled_courses[course_id] = (
                self.courses[course_id].title
            )

            print("Student enrolled successfully.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # ADD LEARNING MODULE
    

    def add_module(self):
        try:
            course_id = input("Enter Course ID: ").strip()

            if course_id not in self.courses:
                raise ValueError("Course does not exist.")

            instructor_id = input("Enter Instructor ID: ").strip()

            if self.courses[course_id].instructor_id != instructor_id:
                raise ValueError(
                    "Only the course instructor can add modules."
                )

            module_id = input("Enter Module ID: ").strip()
            module_name = input("Enter Module Name: ").strip()

            self.courses[course_id].add_module(
                module_id,
                module_name
            )

            print("Learning module added successfully.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # COMPLETE MODULE
    

    def complete_module(self):
        try:
            student_id = input("Enter Student ID: ").strip()
            course_id = input("Enter Course ID: ").strip()

            if student_id not in self.students:
                raise ValueError("Student does not exist.")

            if course_id not in self.courses:
                raise ValueError("Course does not exist.")

            if course_id not in self.enrollments[student_id]:
                raise ValueError("Student is not enrolled.")

            module_id = input("Enter Module ID: ").strip()

            course = self.courses[course_id]

            if module_id not in course.modules:
                raise ValueError("Module does not exist.")

            completed = self.enrollments[student_id][course_id][
                "completed_modules"
            ]

            if module_id not in completed:
                completed.append(module_id)

            self.update_progress(student_id, course_id)

            print("Module marked as completed.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # ADD ASSIGNMENT
    

    def add_assignment(self):
        try:
            course_id = input("Enter Course ID: ").strip()

            if course_id not in self.courses:
                raise ValueError("Course does not exist.")

            instructor_id = input("Enter Instructor ID: ").strip()

            if self.courses[course_id].instructor_id != instructor_id:
                raise ValueError(
                    "Only the course instructor can add assignments."
                )

            assignment_id = input("Enter Assignment ID: ").strip()
            assignment_name = input("Enter Assignment Name: ").strip()

            max_score = int(input("Enter Maximum Score: "))

            if max_score <= 0:
                raise ValueError("Maximum score must be positive.")

            self.courses[course_id].add_assignment(
                assignment_id,
                assignment_name,
                max_score
            )

            print("Assignment added successfully.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # SCORE MANAGEMENT
    

    def enter_score(self):
        try:
            instructor_id = input("Enter Instructor ID: ").strip()
            course_id = input("Enter Course ID: ").strip()

            if course_id not in self.courses:
                raise ValueError("Course does not exist.")

            if self.courses[course_id].instructor_id != instructor_id:
                raise ValueError(
                    "Only the course instructor can enter scores."
                )

            assignment_id = input("Enter Assignment ID: ").strip()

            course = self.courses[course_id]

            if assignment_id not in course.assignments:
                raise ValueError("Assignment does not exist.")

            student_id = input("Enter Student ID: ").strip()

            if student_id not in self.enrollments:
                raise ValueError("Student does not exist.")

            if course_id not in self.enrollments[student_id]:
                raise ValueError("Student is not enrolled.")

            max_score = course.assignments[assignment_id]["max_score"]

            score = float(
                input(f"Enter Score (0-{max_score}): ")
            )

            if score < 0 or score > max_score:
                raise ValueError("Invalid score.")

            course.assignments[assignment_id]["scores"][
                student_id
            ] = score

            self.enrollments[student_id][course_id]["scores"][
                assignment_id
            ] = score

            self.update_progress(student_id, course_id)

            print("Score added successfully.")

            self.save_data()

        except ValueError as e:
            print("Error:", e)

    
    # UPDATE COURSE PROGRESS
    

    def update_progress(self, student_id, course_id):

        course = self.courses[course_id]

        enrollment = self.enrollments[student_id][course_id]

        total_modules = len(course.modules)

        completed_modules = len(
            enrollment["completed_modules"]
        )

        if total_modules == 0:
            module_percentage = 0
        else:
            module_percentage = (
                completed_modules / total_modules
            ) * 100

        enrollment["completion"] = round(
            module_percentage,
            2
        )

    
    # COURSE PROGRESS
    

    def show_progress(self):
        try:
            student_id = input("Enter Student ID: ").strip()
            course_id = input("Enter Course ID: ").strip()

            if student_id not in self.enrollments:
                raise ValueError("Student does not exist.")

            if course_id not in self.enrollments[student_id]:
                raise ValueError("Student is not enrolled in this course.")

            progress = self.enrollments[student_id][course_id]

            print("\n========== COURSE PROGRESS ==========")

            print("Student:",
                  self.students[student_id].name)

            print("Course:",
                  self.courses[course_id].title)

            print(
                "Completed Modules:",
                len(progress["completed_modules"]),
                "/",
                len(self.courses[course_id].modules)
            )

            print(
                "Completion Percentage:",
                progress["completion"],
                "%"
            )

            print("\nScores:")

            if progress["scores"]:
                for assignment_id, score in progress["scores"].items():

                    assignment = self.courses[
                        course_id
                    ].assignments[assignment_id]

                    print(
                        assignment["name"],
                        ":",
                        score,
                        "/",
                        assignment["max_score"]
                    )
            else:
                print("No scores available.")

        except ValueError as e:
            print("Error:", e)

    
    # CERTIFICATE ELIGIBILITY

    def check_certificate(self):
        try:
            student_id = input("Enter Student ID: ").strip()
            course_id = input("Enter Course ID: ").strip()

            if student_id not in self.enrollments:
                raise ValueError("Student does not exist.")

            if course_id not in self.enrollments[student_id]:
                raise ValueError("Student is not enrolled.")

            progress = self.enrollments[
                student_id
            ][course_id]

            completion = progress["completion"]

            if completion >= 100:
                print("\nCertificate Eligibility: ELIGIBLE")
                print("Congratulations!")
            else:
                print("\nCertificate Eligibility: NOT ELIGIBLE")
                print(
                    "Complete the course to receive the certificate."
                )

        except ValueError as e:
            print("Error:", e)


    # DISPLAY ALL COURSES

    
    def display_courses(self):

        if not self.courses:
            print("No courses available.")
            return

        print("\n========== AVAILABLE COURSES ==========")

        for course in self.courses.values():
            course.display()

   
    # DISPLAY STUDENTS
    

    def display_students(self):

        if not self.students:
            print("No students registered.")
            return

        print("\n========== STUDENTS ==========")

        for student in self.students.values():
            student.display()

   
    # DISPLAY INSTRUCTORS
    

    def display_instructors(self):

        if not self.instructors:
            print("No instructors registered.")
            return

        print("\n========== INSTRUCTORS ==========")

        for instructor in self.instructors.values():
            instructor.display()

    
    # TXT FILE HANDLING
    

    def save_data(self):

        try:
            with open("lms_data.txt", "w") as file:

                file.write("ONLINE LEARNING MANAGEMENT SYSTEM\n")
                file.write("=" * 50 + "\n\n")

                file.write("STUDENTS\n")

                for student in self.students.values():

                    file.write(
                        f"{student.user_id} | "
                        f"{student.name} | "
                        f"{student.email}\n"
                    )

                file.write("\nINSTRUCTORS\n")

                for instructor in self.instructors.values():

                    file.write(
                        f"{instructor.user_id} | "
                        f"{instructor.name} | "
                        f"{instructor.email}\n"
                    )

                file.write("\nCOURSES\n")

                for course in self.courses.values():

                    file.write(
                        f"{course.course_id} | "
                        f"{course.title} | "
                        f"Instructor: "
                        f"{course.instructor_id}\n"
                    )

                    file.write("  Modules:\n")

                    for module_id, module in course.modules.items():

                        file.write(
                            f"    {module_id} - "
                            f"{module['name']}\n"
                        )

                    file.write("  Assignments:\n")

                    for assignment_id, assignment in (
                        course.assignments.items()
                    ):

                        file.write(
                            f"    {assignment_id} - "
                            f"{assignment['name']} - "
                            f"Max Score: "
                            f"{assignment['max_score']}\n"
                        )

            print("Data saved to lms_data.txt")

        except Exception as e:
            print("File error:", e)

    
    # LOAD FILE
    

    def load_data(self):

        if os.path.exists("lms_data.txt"):
            print("Previous LMS data file found.")

        else:
            print("Starting new LMS system.")



# MAIN MENU


def main():

    lms = LMS()

    while True:

        print("\n")
        print("=" * 55)
        print("       ONLINE LEARNING MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Student Registration")
        print("2. Instructor Registration")
        print("3. Course Creation")
        print("4. Course Enrollment")
        print("5. Add Learning Module")
        print("6. Complete Learning Module")
        print("7. Add Assignment")
        print("8. Enter Assignment Score")
        print("9. View Course Progress")
        print("10. Check Certificate Eligibility")
        print("11. Display All Courses")
        print("12. Display All Students")
        print("13. Display All Instructors")
        print("14. Save Data")
        print("15. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            lms.register_student()

        elif choice == "2":
            lms.register_instructor()

        elif choice == "3":
            lms.create_course()

        elif choice == "4":
            lms.enroll_student()

        elif choice == "5":
            lms.add_module()

        elif choice == "6":
            lms.complete_module()

        elif choice == "7":
            lms.add_assignment()

        elif choice == "8":
            lms.enter_score()

        elif choice == "9":
            lms.show_progress()

        elif choice == "10":
            lms.check_certificate()

        elif choice == "11":
            lms.display_courses()

        elif choice == "12":
            lms.display_students()

        elif choice == "13":
            lms.display_instructors()

        elif choice == "14":
            lms.save_data()

        elif choice == "15":
            print("Thank you for using LMS.")
            lms.save_data()
            break

        else:
            print("Invalid choice. Please try again.")



# PROGRAM START


if __name__ == "__main__":
    main()
