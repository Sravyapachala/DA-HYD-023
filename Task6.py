#Task-1: Student Marks Manager

marks=[]
for i in range(3):
    mark=int(input("enter marks:"))
    marks.append(mark)
print("Marks:",marks)
marks.insert(0,90)
marks.extend([75,85])
print("marks:",marks)
if 90 in marks:
    marks.remove(90)
    print("marks:",marks)
print(marks.pop())
print("Final marks:",marks)
print("Length of marks:",len(marks))



#Task-2:Number List Analyser
'''
numbers = [20, 10, 30, 20, 40, 20]
numbers.sort()
print("Ascending order:",numbers)
numbers.reverse()
print("Descending order:",numbers)

n=int(input("enter number:"))
if n in numbers:
    print("Number exists")
    count=numbers.count(n)
    print("Count:",count)
    i=numbers.index(n)
    print("Index:",i)
else:
    print("number does not exist")
small_value=min(numbers)
print("Smallest value:",small_value)
large_value=max(numbers)
print("Largest value:",large_value)
total=sum(numbers)
print("Total:",total)
'''    

#Task-3: Even and Odd Number Separator
'''
numbers = [10, 15, 20, 25, 30, 35] 
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
        print("Even:",even)
    elif i%2!=0:
        odd.append(i)
        print("Odd:",odd)
print(numbers[0:3])
print(numbers[3:])
backup=numbers.copy()
print(backup)
numbers.clear()
print(numbers)
print(backup)
'''

#Task-4: Unique Name Manager 
'''
names = ["Chinnu", "sravya", "Harsha", "Priya", "Rahul"]
name=set(names)
print(name)2
new="Meera"
name.add(new)
print(name)
name.update(("Arun","Priya"))
print(name)
if "Priya" in name:
    name.remove("Priya")
    print(name)
name.discard("Rahul")
print(name)
for i in name:
    print(i)
'''

#Task-5: Course Student Comparison 
'''
python_students = {"Sravya", "Rahul", "Harsha", "Chinnu"}
da_students = {"Rahul", "Chinnu", "Harsha"} 
union = python_students.union(da_students)
print("Union:", union)
common = python_students.intersection(da_students)
print("Intersection:", common)
differ = python_students.difference(da_students)
print("Difference:", differ)
symmetric_differ = python_students.symmetric_difference(da_students)
print("Symmetric:", symmetric_differ)
subset = da_students.issubset(python_students)
print("Subset:", subset)
superset = python_students.issuperset(da_students)
print("Superset:", superset)
disjoint = python_students.isdisjoint(da_students)
print("Both are Disjoint:", disjoint)

for i in python_students.union(da_students):
    print(i)
print("Common students:")
for i in python_students.intersection(da_students):
    print(i)
'''
