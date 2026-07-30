#Numeric datatype --> int,float,complex along with boolean

#Input formatting -->Accepting input from the user --> input()
'''
#accepting integer input from user
#by default input() accepts any input-->str
#int(input()) --> will accept only integers
age = int(input("Enter the age"))
print(age)
print(type(age))

#float(input())--> accepts integers ,float values
grams = float(input("Enter grams "))
print(grams)
print(type(grams))


#Accepting string input from user

name = input("Enter the name:")
print(name)
print(type(name))


#Accept gorup of values

a = input().split()#by default split() has space
print(a)

#space separated values
a = input().split()#now you enter spaces in output
#comma separated values

a = input("Enter the values:").split()
print(a)

a = input("Enter the values:").split(',')
print(a)


# List of integers
marks = list(map(int,input("Enter the values").split(',')))
print(marks)


#Now we want to accept 2 values from user
age,salary = map(int,input("Enter the values").split(','))
print(age)
print(salary)

#Single input --> int(input())
#two inputs -->a,b = map(int,input().split(','))
#any number results as list --> a = list9map9int,input().split(',')))
            
#group of float values
age,salary = map(float,input("Enter the values").split(','))
print(age)
print(salary)

#float of integers
marks = list(map(float,input("Enter the values").split(',')))
print(marks)

#Accepting input from user --> int,float --> input formating

#operaters --> operaters perfoem operatioms between values (operends)
#7 types -->Arthmetic,assignment,comparision(Relationship)
#Membership,Identity,Logical,Bitwise

#Arthemetic Operations --> Arthmetic operations
#+,-,*,/

print(5+3)
print(5-2)
print(5*2)
print(5/2)#float value
#Floor division (integer division) --> return quotient


print(5/3)
#floor division (Integer division)-->returns quotient
print(5//3)
#modules-->divisible rules --> returns remainder
print(5*3)
#power (exponential)
print(5**3)

#Task -->accept inetger input as length,breadth -->find the area of rectangle
#Area = length * breadth


length,breadth = map(int,input("Enter the values").split(','))
print(length * breadth) 

#Assignment operaters --> assign the values
# = , += ,-=

a=45
print(a)
#update the value of a
a = a + 5 #a += 5
print(a)

b = 35
b += a # b = b+a
print(b)
b -= 5 #b = b -5
print(b)

#Task : *=,/=,//=,%=,**= workout

# comparision operaters --> we compare the values --> boolean
# == (equal to), != (not equal to ,<(less than ), > (greater than)
#<= (less than or equal to)>= ( greater than or equal to)

age = 25
print(age == 25) # return boolean output
print(age != 35)
print(age >25)
print(age<20)
print(age >= 25)
print(age <= 35)

print(-5 < -1)


#Membership operaters --> in ,not in -->boolean
#it checks for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)
#print(35 in 355)#typeError

print(25 not in marks)
print('$' in 'abc$%^')


#Logical operaters --> logical decision making --> and,or,not
#and --> all conditions to be satisfied
#or --> any one condition to be satisfied

a = (25 in [25,62,52]) and 45 < 56
print(a)
b = 45 > 56 or 25 <= 45
print(b)
c = not(True)
print(c)
'''


#Identity operators --> check for identity of an object --> id()
#is , is not

a = 35
b = 35
print(id(a))
print(id(b))
print(a is b )
c = a
print(id(c))
print(c is a)

















