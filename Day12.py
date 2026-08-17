'''
Mapping --> Dictionary-->Collection of key-value pairs used to store
related data -->JSON,APIs,Database records

dict() --> data = {} --> data = {key : value}
Dictionary is mutable,Indexed through keys,ordered,Heterogenous,
keys must be unique  (int,strings,float values....)
'''
details = {}
print(type(details))

details = {'Ids':'CGH4022','Name': 'Sravya',
           'Gender':'F','Age':22,
           'Batch':'DA23','Place':'Hyd'}

print(details)
print(len(details))

#Access the data from dictionary
#details[0] #keyError


print(details.keys()) #it returns key from the dictionary
print(details['Ids'],details['Name'])
#if key name is not matching / invalid
#print(details['marks'])#keyError as marks is not present
details['marks'] = []
print(details)
print(type(details['marks']))

details['marks'].append(20)
print(details)
details['marks'].extend([56,25,26])
print(details)

#create key-value pair of practice session
details['PS'] = ('Tuesday','Thursday','Saturday')

print(details.keys())

#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day marks of practice session

print(details['PS'][1])
details['MI'] = ('Monday','Wednesday','Friday')
#operations --> mutable,indexing through keys,membership

print('Wednesday' in details)
print('MI' in details)#returns True as aswe have MI as key
'''for i in details:
    print(i)#returns key one by one

for i in details.keys():
    #print(f'key = {i}')
    print(f'Value = {details[i]}')
    


#keys() --> returns keys from the dictionary


for i in details.values():#returns value from dictionary
    print(i)
 
for i in details.items():#retuns a key-value pair in tuple
    print(i)


for key,value in details.items():
    print(f'key is {key}')
    print(f'value is {value}')


#update() --> updating the dictionary with key-value pairs
details.update({'marks':[],
                'PS':('Tuesday','Thursday','Saturday')})
print(details)
details['marks'].extend([25,65,23])
print(details)
marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)

'''
print(details.keys())
print(details.get('Name'))
print(details.get('Branch'))#it returns None as we dont have branch asa key 
print(details.keys())

details.setdefault('Branch','ECE')#if key is not present it insert into dict
print(details)
details['Branch'] = 'CSE'
print(details)

print(details.setdefault('Name'))
print(details.keys())

print(details.pop('Branch'))#we need to mention key
print(details.keys())

print(details.popitems())#removes and return a key ,value pair as a 2-tuple
print(details.popitems())


del details['Id']
print(details.keys())

details.clear()#removea all elements from D
print(details)

#fromkeys() --> creates a dictionary from iterable (lists,tuples,sets,string)

data = ['sravya','chinnu','data']
b = dict.fromkeys(data)#Create a dict but value set to none
print(b)
b['sravya'] = 22
print(b)

c = dict.fromkeys(['CGH1234','CGH2345'],['code','gnan'])
print(c)


#task :create a dictionary with your personal details,similar to your
#codegnan profile












































    





























