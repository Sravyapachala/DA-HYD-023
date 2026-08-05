'''
Tokens --> Keywords,Identifiers,Literals,Operaters,Puncuaters,variables
Operators --> Numeric data(int,float,complex),bool
Control Flow --> if,elif,else,for,while
Sequence --> Strings,lists,sets,tuples,mapping(dict)

#Strings --> Group of charecters,we use single or double or triple quotes
#for representation of strings...
#Strings are Immutable,Ordered,Indexed,Collection
#space is also a charecter
name = 'Sravya'
print(name)
print(type(name))
print(len(name)) #len -->returns the number of items in container

#index() --> fetch the object(position) starts at 0 and ends at len(obj)- 1
#we use [] representation
print(name[0])
print(name[5])
#print(name[25])#IndexError --> as its out of range

#Negative indexing --> -1 to len(obj)
print(name[-1]) #it returns last charecter
print(name[-3])
print(name[-33])
#Slicing --> we can access group of charecters(objects)
#we can [start:end] #start default --> 0,start is included,end is excluded
name = 'Sravyapachala'
print(name[:]) #return entire string
print(name[0:]) #returns entire string
print(name[:4]) #starts at 0th index before 4th index
print(name[1:5])
print(name[4:])

name = 'python'
print(name[3:7])
print(name[7:3]) #returns empty as strings are immutable
#Slicing ia applicable from lower index to higher index
print(name[:45]) #return till end of the string
print(name[45:])


name = 'python'
print(name[-1:-5]) #return empty string
print(name[-5:-1]) #starts at -5 and ends at -2
#print 'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])


print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve , -ve,-ve & +ve,-ve all posibilities
'''
'''
course = 'Data Analysis'
print(len(course))
#Data --> result
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1]) #retrun all charecters
print(course[:2]) #includes start to end skipping 1 charecter

print(course[1:6:3]) #[1:6] -->ataAn --> [1:6:3]--> aA

print(course[2:3])

print(course[::-1])#it returns the reverse of a string
print(course[::-2])

#Task : workout with all possibilities of slicing and striding on a example


name = 'codegnan'
#name[3] = 'w' #strings are immutable

#Operations on strings --> Indexing,Concatenation,Repetition
print(name * 3)
print('*' * 25)#repetition

#Concatenation --> combining strings

data = 'saketh' + 'python' +' '+'database'
print(data)
print('123' * 4) #Numeric String
print('code' in 'codegnan')

for i in 'codgnan':
    print(i,':')
#in above case we get every charecter line by line

for i in 'codgnan':
    print(i,end=' ')

'''
name = "codgnan"
#Built-in functions -->len(),min(),max(),sorted()
print(len(name))
print(min(name)) #alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(chr(97))
print(max(name))
print(sorted(name)) #return a list by sorting all elements

#Methods on strings --> case-conversions,Finding/searching...
name = 'Codgnan data'
#Case-conversions -->upper(),lower(),title(),capitalze()
a = name.upper()
print(a)
b = name.lower()
print(b)
#Capitalize() --> converts first letter to uppercase

c = name.capitalize()
print(c)
d = name.title() #converts every work first letter to uppercase
print(d)


#Task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A - Z





















































