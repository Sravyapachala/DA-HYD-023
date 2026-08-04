'''
marks = int(input ("Enter the marks:"))
if marks > 100 or marks < 0:
    print("Invalid marks entered")
elif marks >= 90:
    print("Grade: A")
    print("Remark: Outstanding!")
elif marks >= 80:
    print("Grade: B")
    print("Remark: Execellent!")
elif marks >= 70:
    print("Grade: C")
    print("Remark: Good")
elif marks >= 60:
    print("Grade: D")
    print("Remark: Fail, needs Improvement")
elif marks >=50:
    print("Grade: E")
    print("Remark: Poor , needs serious improvement")
else:
    print("Grade: Fail")
    print("Remark: Failed, needs to Rrappear")
'''
#EVEN - ODD CHECKER(WITH TWIST)
'''
num = int(input("Enter a number:"))
if num == 0:
    print("zero is neither even nor odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even Number")
elif num < 0 and num % 2 != 0:
    print("Negative Odd Number")
elif num > 0 and num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
'''
#SEASON IDENTIFIER
month = int(input("Enter month number:"))
if month < 1 or month > 12:
    print("Invaild Month entered")
elif month == 12 or month == 1 or month == 2:
    print("Season: Winter")
elif month == 3 or month == 4 or month == 5:
    print("Season: Summer")
elif month == 6 or month == 7 or month == 8:
    print("Season: Spring")
else:
    print("Season: Autumn")
