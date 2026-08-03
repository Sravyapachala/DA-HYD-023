'''
Identity Operaters --> It checks the identity of an objectc --> id()
#is,is not 

a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)

a =[1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))

# As we have lists(mutable Collection) both c and a lists will have different values
#ids whereas values are same 
print(c is a)  #Output false
print(c == a)  #Output true
print(a is not c)


#Bitwise Operaters --> We perform bitwise operations over operants
#& (and) , | (or) ,^(XOR),shifting operaters (<<,>>)
# Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and us performed

print(5|3) # bitwise OR

print(5^3) #Bitwise XOR

print(5 and 3) #here and is logical operaters checks for the both existances
#return 5 in above case

print(5 or 3)# return 3 in this case 


#Leftshift operetaers <<,Right shift operator >>

print(5<1) #False comparession
print(5 << 1) # left shift operation by 1 position
print(5 >> 1) #Right shift operation


print(15 << 2) # convert 15 to binary and perform 2 times shifting

print(15 >> 2) # same 2 times right shifting 

# Input Formatting --> input(),int(input()),float(input())
#you know --> single input
# 2 or 3 inputs --> map()
#group of integer --> list(map(int,input().split(','))

name = input("Enter the names:").split(',')
print(name)

name1,name2 =map(str,input("Enter the friends Names:").split(','))
print(name1,name2)
'''
#Tokens --> Numeric Datatypes --> Operators -->Flow of the program
#Control Block Statement
#When to execute,how to execute
#Conditional statement --> if,else,elif(rely on condition to be executed)
#reputition statements(Loops) --> for,while

#Conditional statements --> if usage
'''
Syntax :

if <condition> :
    statements(s).....
    ......

#age = 15
age = int(input("Enter the age:"))
if age > 18:
    print('your age is:',age)

age = int(input("Enter your age :"))
if age>=18 and age in [19,21,25]:
    print('your age is ',age)
print(age)

#else keyword --> if - else

else:
    statement(s)....

if -else usage as below:

if <condition>:
    statement(s)....
    ....
else:
    statement(s)....
    ....

#vote Eligibilty -> to check his/her voter eligibility and give access....

age = int(input("Enter the age:"))
if age>=18:
    print("You have voter eligiblity and age is",age)
    print("Access Granted")
else:
    age = 18-age
   # print("You dont have eligibility as your age is",age,"years")
    print("You need to wait for more",age,"years")

#same case lets use only nested --> if,else
if age >0:
    if age>=18:
        print("You have voter eligiblity and age is",age)
        print("Access Granted")
    else:
        age = 18-age
   # print("You dont have eligibility as your age is",age,"years")
        print("You need to wait for more",age,"years")
else:
    print("you have entered -ve values/zero enter only +ve")


Task : Student marks and grade analyzer
90 - 100 --> 'grade A'
80 - 89 --> 'grade B'
70 - 79 --> 'grade c'
60 - 69 --> 'grade D'
>60 --> Fail
#also -ve cases should not be allowed and marks shoudnt be grater than 100
'''









































































