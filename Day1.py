#IDLE is a color coding enviraonment
#hastag is used as a singlr line comment
#we use trip;e quotes (single/double) ''',""" as multiline comment
#print('Hello Sravya')


'''
Tokens --> A smallest unit in a program. there are 5 types of tokens..
-> keywords
->identifiers
->literals
->operaters
->punctuaters
'''
#keywords --> These are reserved words in pyhton. We have 35 keywords..
#help()-->keywords -->it gives 35 keywords --> True,False
#We can start with uppercase/lowercase letters (A-Z,a-z) but not special charecters
#@,#,$...
#No space between letters,where as we can also use underscore as an identifier_
#python is a case sensitive language 
name ='sravya'
print(name)
email_id = 'sravyapachala04@gmail.com'
print(email_id)
#@mail = 'sravya26@gmail.com'
#print(@mail)           --> python is case-sensitive it will throwNameError
batch ='da23'
print(batch)
#variable --> named memory location where we store the data;its a placeholder 
batch = 'IT'
print(batch)
#Literala --> These are constants (value(s)) -->number,charecter
#operaters --> operaters perform specific operation --> 7 types
length = 5
breadth = 3
area = length * breadth
print(area)

#Multiassignments of variables
name ='codegnan'
print(name)
name,location,age = 'codegnan','Hyd',7
print(name)
print(location)
print(age)
