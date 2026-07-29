'''
Tokens --> Variables,Punctuators

Variables-->  Named memory location,its a placeholder for data
#rules are to be followed

#MultiAssignment of variables

name,age,place ='Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep='/')
print(name,age,place,sep='-------->')


#a,b = 2,4,5 #valueError as too many values to unpack
#Reassigning variables

#name ='codegnan'
#a,b = 45,1.5
#print(a,b)
#a,b = b,a#swapping
#print(a,b,sep=',')

#a,b = b,c#nameError as c is not defined
#print(a,b)


#deletiong the variables -->del
#del a
#print(a)
#del a,b
#print(a,b)

#Punctuators --> [](Lists),()(Tuples),{}(Dict,sets)
name = "Codegnan";age = 7;course ='Data_Analysis'
print(name,age,course)

#DataTypes --> Numeric (int,float,complex),boolean,None,
           #--->Sequences -->Lists,Tuples,sets,strings,
             #        Frozensets,mappings(dict)

#Numeric  type --> int,float,complex
#int datatype --> quantity
age = 7
print(age)
print(type(age)) #type --> returns the datatype of object

print(type(234))

#quantity = 03 #it is not allowed
#print(auantity)
#float datatype --> temp,salary,price

price = 750.24;discount = 2.5
print(price,discount)
print(type(price))


#complex -->combination of real and imag
data = 5 + 2i
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))


#Boolean --> True/False
valid = True
print(type(valid))

error = False
print(tyoe(error))


#TypeCasting --> Converting one type to another type
#python by default follows implicit type(we need not mention the datatype)

#we will go for Explicit Converstion

#every built-in datatype is a built-in function
int,float,complex,bool

#Typecasting --> int -->float,complex,bool

price = 63.2
print(type(price))
b = int(price)
print(b)
c = complex(price)
print(c)
d = bool(price)
print(d)

#complex -->Typecasting -->int,float,bool
data = 2+5j
print(type(data))
#b = int(data)#TypeError
#print(data)
#c =float(data)
#print(c)
d = bool(data)
print(d)
print(type(d))



e = int(float(bool(45)))
print(e)
'''
f = 45 + 2.5 + 3j + False
print(f)















