'''
Tokens,Datatypes --> control Flow Statements --> if,else,elif,for,while,break
continue...

Procedure Oriented programming

Functions --> A function is a ablock of code which performs a specific task
Its a reusable group of statements where we define using
def keyword
Advantages --> Code reusability,code maintainability,ease of debuggin,avoiding
code duplication,modularity

def fname(parameters): Function def
    """Doc String"""    Description
    statement(s)....
    ..........          Function body
    return value(s)....
fname(args)            Function call

#To perform sum of given objects
def add(a,b):
    """Sum of objects"""
    c = a + b
    return c
print(add(12,3)) #Addition 
print(add('code','gnan')) #concatination
print(add([12,5],[12,35])) #Merging
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)) #it returns results along with none

name,age,salary = "Sravya",22,50000
#usage of return

def details():
    #return name,age,salary
    #return "Codegnan"
    #return 23+34+45
    return    #it returns None asa output
print(details())

There are 5 types of arguments:

--> Positional Arguments
--> Default arguments
--> keyword arguments
--> Variable lenght arguments(*args)
--> keyword variable length arguments (**kwargs)

#Positional Arguments --> Number of arguments in functoion in function defn should
#match with function call (order has to be maintained)


def details(name,place):
    """To store the details"""
    #name = "Codegnan"
    #place = "Hyderabad
    return name,place
print(details("Sravya","Codegnan"))
print(details("Lalli","Vizag"))
#print(details("Vizag","Harsha",34)) #raises TypeError as only 2 arguments to take
c,d = map(str,input("Enter the values").split(','))
details(c,d)



#Default arguments --> we can make arguments asa default but not first argument
#as default

#def grocery(item,price=35):
def grocery(item="Cheese",price = 100):#we can also make all args as default
    """usage of default arguments"""
    print(f'The items is {item} and price is {price}')

grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread") #by default we have given price as 35
grocery() #as both items and price asa default arguments

'''

#keyword arguments --> whenever we want to specify the name of argument
def employee(name,salary,role,place="Codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary},works in {place}')
employee("sai",20000,"Admin")
employee(salary = 25000,role = "Frontdesk",name = "Sravya")
employee("Lalli",25000,"IT","Cognizant")





































































