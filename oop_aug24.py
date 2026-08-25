'''
OOP--> Class,Object,Methods (__init__())
Encapsulation -->Public,Protected,Private
Inheritance --> It is one of key feature of OOP where we inheritant 
the properties (attributes/methods) from one class to another class
(base class(parent class) --> derived class(child class))
whatsapp --> Personal User,Bussiness User (catalog),community Add
Features --> Code Reuseablility,Avoiding code duplication,
code maintainability,Polymorphism (Method Overriding(super()),Method Overloading,Operator Over loading__add__,__str__)

Types : Single Inheritance (Finger Print)
-->One child class inheriting properties from one parent class
Multiple Inheritance(Mother,Father-->Child) --> One child 
class inheriting properties from two parent classes
Multilevel Inheritance (GrandParent -->Parent --> child)
level by level
Hierarchical Inheritance --> multiple child classes
inheriting properties from single parent 
Hybrid Inheritance --> It can carry one or more type of inheritance 
Syntax:

single Inheritance:

class baseclasses:
    statement(s)..
    .....
class Derivedclass(baseclass):
    ........
    .....
'''
'''
class User:
    """Single Inheritance usage"""
    def send_message(self):
        print('Sending Message')
    def voice_call(self):
        print('Making Voice Calls')
    def video_call(self):
        print("making video calls")
class BusinessUser(User):
    #pass
    def create_catalog(self):
u1 = BusinessUser()
print(dir(u1))
u1.send_message()
u1.video call()
u1.voice call()
u1.create catalog()

'''
'''
#social Media Login --> users --> updates_users
class Users:
    """Single Inheritance usage"""
    company ="Codegnan" #class attribute
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + self.lname
#u1 = Users("Sravya","Pachala")
#print(u1.full_name())
#print(u1.company)
class update_users(Users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1 = update_users("Sravya","Pachala")
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2 = Users("sai","taripodu")
print(u2.full_name())
print(u2.company)

'''
'''
#what if we have constructer in child class also....
#Father --> Kid(property)

class Father:
    """Usage of constucter in single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now childclass will have constructor"""
    def __init__(self):
        #self.property = 200000
        self.cash = 200000
    def kid_property(self):
        print(f'Kid property is {self.property}')
obj = Kid()
obj.father_property()
obj.kid_property()
#in the above case it is giving same value for father also as 
#2lakhs ...when we gave property asa same attribute in both classes



#in above case both parent and cchild have constucter so the constructer overriding is happending even the attributes are different
#super()
#-->super().__init__()
#-->super().__init__(args)
#-->super().method() -->method overriding

#constructer overriding is happening --> super() usage
#in above example we use super()
'''
class Father:
    """Usage of constucter in single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')

class Kid(Father):
    """Now childclass will have constructor"""
    def __init__(self):
        super().__init__() #calling superclass constucter
        self.cash = 200000
    def kid_property(self):
        print(f'Kid property is {self.property}')
        print(f'Kid Final property is{self.cash + self.property}')
obj = Kid()
obj.father_property()
obj.kid_property()
