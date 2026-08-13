'''
Lists,Tuples...


#List --> Mutable,Ordered,Heterogenous

#index(),count(),copy(),sort(),reverse()

details = ['codegnan',7,2018,'Hyderbad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21)) #it returns first occcurence
print(details.index(21,6))
print(details.index('python')) #ValueError

print(details.count(21))
print(details.count('python')) #it return 0 as we dont have it

'''
data = ['codegnan','sravya','python','java']#input
#output should be as follows
'''
0 : codegnan
1 : sravya
2 : python
3 : java


for obj in data:
    print(':',obj)

for obj in range(len(data)):
    print(obj,':',data[obj])
    

#copy()--> shaloow copy of the given collection

new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('Sravya')
print(data)
print(new)


data = [1,4,5,[21,34,45],24]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents' #whenever we make changes in nested list original will also be affected

print(new)
print(data)

new[1] = 'Python'
print(new)
print(data)


marks = [14,24,-45,27,35]
print(marks)
#print(marks.sort()) #return None
#print(marks) #returns in ascending order
#marks.sort(reverse = True) #returns in Descending order....
#print(marks)

marks.insert(2,'code')
#marks.sort()
#reverse() --> returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])

#type(),len(),max(),min(),print()

print(sorted('codegnan'))#returns list in ascending order
#print(sorted(['code','23',34,45]))#raises Error

#Tuples --> Tuples are Indexed,Ordered,Heteogenous,Immutable collection,dimensions
#coordinates,database records,we prefer () for tuple notat

a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))


#operations --> Indexing,slicing,striding,membership,merging,repetion

courses = ('PFS','JFS','DS'),'AgenticAi',[100,6,6])
print(courses)
print(len(courses))

print(courses[-2][-2:])
#courses[2] = 23 Tuples are immutable
courses[-1].append('codegnan') #we can make any modifications inside list
print(courses)

#Create a nested tuple as above and work on sliciing ,striding and list function
print('PFS' in courses) #Membership
d = courses * 2 #repetition
print(d)
e = courses + (2,3,4,5) #merging
print(e)


#Tuples Immutable -->count(),index()
print(courses.index('AgenticAI'))#returns first occurence
print(courses.count('Agents'))

#print(courses.sort()) #attributeError --> sort() is in lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

#typeCasting
d = tuple(sorted((23,12,3,4,5)))
print(d)


#accept group of integers space separated
a,b = map(int,input("Enter the values").split())
print(a,b)

a = tuple(map(int,input("Enter the values").split(',')))
print(a)


print('9+4')
print(eval('9+4'))

a = eval(input("Enter a list")) #in this case u can exactly enter data as l:
print(a)
print(type(a))

'''
#Task:Take a auser input as string,do this in 2 ways
'''
1: give the count of each repeating charecters
test case 1:programming
 r is repeating 2 times
 g is repeating 2 times
 m is repeating 2 times
 
2:
test case 1:programming
 r is repeating 2 times
 index = [1,4]
 g is repeating 2 times
 index = [3,10]
 m is repeating 2 times
 index = [6,7]
'''
















































































































