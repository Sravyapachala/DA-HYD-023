'''
#Text case converter

text = input("Enter a sentence: ")

methods = [
    ("Upper", text.upper()),
    ("Lower", text.lower()),
    ("Title", text.title()),
    ("Capitalized", text.capitalize()),
    ("Swap case", text.swapcase())
]

for name, result in methods:
    print(name, ":", result)

if text.isupper():
    print("Original text is UPPER CASE")
elif text.islower():
    print("Original text is lower case")
elif text.istitle():
    print("Original text is Title Case")
else:
    print("Original text is Mixed Case")

print("isupper():", text.isupper())
print("islower():", text.islower())
print("istitle():", text.istitle())


#Username Validator

while True:
    username = input("Enter username (or quit): ")

    if username.lower() == "quit":
        break

    if username.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Does not contain only letters and numbers")

    if username[0].isalpha():
        print("Begins with a letter")
    else:
        print("Does not begin with a letter")

    if username.isidentifier():
        print("Valid Python identifier")
    else:
        print("Invalid Python identifier")

    if username.isascii():
        print("Contains only ASCII characters")
    else:
        print("Contains non-ASCII characters")

    print()


#Formatted Student Report

students = []

for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks")
        continue

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students.append((name, marks, grade))

print("\n" + "STUDENT REPORT".center(30))
print("=" * 30)
print(f"{'Name'.ljust(15)}{'Marks'.rjust(7)}{'Grade'.rjust(8)}")

for name, marks, grade in students:
    print(f"{name.ljust(15)}{str(marks).rjust(7)}{grade.rjust(8)}")

'''


#Charecter and Text Analyser

text = input("Enter text: ")

letters = digits = spaces = printable = non_printable = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    if ch.isdigit():
        digits += 1
    if ch.isspace():
        spaces += 1
    if ch.isprintable():
        printable += 1
    else:
        non_printable += 1

print("\n--- Text Analysis ---")
print(f"Letters      : {letters}")
print(f"Digits       : {digits}")
print(f"Spaces       : {spaces}")
print(f"Printable    : {printable}")
print(f"Non-printable: {non_printable}")
print(f"Lower case   : {text.islower()}")
print(f"Upper case   : {text.isupper()}")
print(f"Title case   : {text.istitle()}")


    



































