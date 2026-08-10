'''
Strings --> CaseConversions,searching & Finding,strings testing methods,
Replace,space removal

#Searching,Finding,Replacing,Joining...
a = "Codgnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g')#it returns the index position
print(b)
c = a.index('n')#it returns the first occurence
print(c)
d = a.index('n',6)#it returns the next occurence
print(d)
#e = a.index('n',8)#value error
#print(e)
#f = a.index('t')#valueError
#print(f)
g = a.index('n',2,6)
print(g)

#rindex()-->returns last occurence
b = a.rindex('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8) #it returns valueError
#print(d)


#count(0 -->returns thye number of items object is representing

print('Codegnan'.count('n'))
print('code'.count('w')) #it return 0 as we dont have 'w' in 'code'
print('Cakshjasaksajs'.count('a'))


#find() --> first occurence but it avoid error returns -1 if substring is
#not found
print('codegnan'.find('r')) #it returns -1

print('codegnan'.find('n'))

print('codegnan'.rfind('n'))

'''
'''
a = "DataAnalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))
    

#Replacing,Splitting,Joining

#Strings are immutable
a = 'Cogegnan'
#a[4] = 's'
print(a.replace('g','s'))
a = a.replace('g','s')
print(a)
print('ffrfjergftegvfkjegcf6tsvfjkeruy'.replace('#',''))
print(a.replace('X','Sravya'))

'''
'''
a = 'code sravya python'
print(len(a))
b = a.split()#by default if we have space it splits (returns list)
print(b)
print(len(b))
c = 'code,sravya,python'
d = c.split()
print(d)
e = c.split(',')
print(e)


#join()

a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('sravya'))
print(' '.join('sravya'))

#String testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...

a = 'Codgnan123'
print(a.isalnum())#return True for alphanumeric strings else False
b = 'Codegnan'
print(b.isalnum())
print(a.isalpha())#return True only for alphabets
print(a.isdigit())#return True only for digit string
print('7670178445'.isdigit())
print('4568'.isnumeric())#this has upper edge(numbers,fractions,romans)
#startswith() -->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))


print('codegnan'.islower())#returns True for all lowercase
print('codegnan'.isupper())#return True for all uppercase
print('codegnan Python'.istitle())

#Space removal --> strip()(removes leading and trailing spaces)

a = 'codegnan'
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)

'''
#zfill() filling with zeros as per the given numeric string

print('234'.zfill(4))
print('234',zfill(7))
#center(),ljust(),rjust() -->Alignment of strings(check lenght and then modify the width accordingly)
print('hai'.center(6)

print('hai'.center(6,'#'))
print('hai'.center(6,'#'))






































































































