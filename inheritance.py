# inheritance means a if class(parents) methds or property are using a child class are called the inheritance :
"""class father():
    def father_name(self):
        print("call father class ...")

class child(father):
    def child_name(self):
        print("call the child classs....")

obj1=father()
obj1.father_name()"""




"""class parents():
    def mobile(self):
        print("the parents are using a nokia mobile..")

class child(parents):
    def laptop(self):
        print("you are using a dell laptop...")


c1=child()
c1.laptop()"""

# (constructor base) if a parents class have constructor but a child class not having any constructor then its call only the parents class costructor as:

"""class person():
    def __init__(self):
        print("call the person constructor..")
    
class child(person):
     pass

obj=child()"""

#if parents and child class both having their constructor then the child class call own constructor and ovveride to the parents constructor as:
"""class person():
    def __init__(self):
        print("call the person constructor..")
    
class child(person):
     def __init__(self):
         print("cal the child constructor")

obj=child()"""

#if you want to both construtor calling then you use the super method as:
"""class person():
    def __init__(self):
        print("call the person constructor..")
    
class child(person):
    def __init__(self):
        super().__init__()
        print("cal the child constructor")

obj=child()"""

# practice questions on inheritence:

"""class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


class manager(employee):
    def __init__(self,name,salary,Role):
        super().__init__(name,salary)
        self.Role=Role

m1=manager("Ritik_upadhyay","50000","Data scientist")
print("Name:",m1.name)
print("Salary:",m1.salary)
print("Role:",m1.Role)"""



# There are three part of inheritence 
# single level inheritance(inheritance)
# muti-level_inheritance
# multiple inhritance

# single inheritence means only one parents class method or proprty are using through a child class as:

"""class father():
    def father_class(self):
        print("call father class..")

class child(father):
    def child_name(self):
        print("call the child class..")

c1=child()
c1.child_name()
c1.father_class()"""

# single inheritence with constructor:

"""class car():
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

class brande(car):
    def __init__(self,name,colour,brand):
     super().__init__(name,colour)
     self.brand=brand

c1=brande("scorpio","black","2020")
print("NAME=",c1.name)
print("COLOUR=",c1.colour)
print("BRAND=",c1.brand)"""

#example of mutilevel-inheritance:

"""class grandfather():
    def house(self):
        print("i have a big house..")

class father(grandfather):
    def car(self):
        print("i have super car..")

class son(father):
    def mobile(self):
        print("i have a new mobile!..")

class child(son):
    def laptop(self):
        print("i have a new dell laptop...")

c1=child()
c1.laptop()
c1.mobile()
c1.car()
c1.house()"""

"""class college():
    def college_name(self):
        print("students college name is DIET....")

class studentsA(college):
    def studentsa(self):
        print("thre are b.tech course in DIET")

class studentsB(studentsA):
    def studentsb(self):
        print("there are BCA course is in DIET")

class studentsC(studentsB):
    def studentsc(self):
        print("There are BBA course is in DIET..")


sc=studentsC()
sc.college_name()
sc.studentsa()
sc.studentsc()            
sc.studentsb()
sc.studentsc() """     


#create a university system Which having three class Person with some information(NAME,AGE,ADDRESS),Employee with some information(employee_id,slary):
#and a class professor with infromation(SUBJECT,DEPARTMENT):

"""class person():
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

class employee(person):
    def __init__(self,name,age,address,employee_id,salary):
        super().__init__(name,age,address)
        self.salary=salary
        self.employee_id=employee_id

class professor(employee):
    def __init__(self,name,age,address,salary,employee_id,subject,department):
        super().__init__(name,age,address,employee_id,salary)
        self.subject=subject
        self.department=department

p1=professor("Ritik_upadhyay","21","Budhana","251309","50000","python_programming","Teaching")
print("name:",p1.name)
print("age:",p1.age)
print("address:",p1.address)
print("salalry:",p1.salary)
print("subject:",p1.subject)
print("Department:",p1.department)"""

#multiple  inheritenece

#we can written as multiple inheritence:

# Parent 1
"""class Father:
    def work(self):
        print("Father works hard")

# Parent 2
class Mother():
    def care(self):
        print("Mother cares")

# Child class (inherits from both)
class Child(Father,Mother):
    def play(self):
        print("Child plays")

c1=Child()
c1.work()
c1.care()
c1.play()"""



"""class Father():
    def __init__(self):
        print("Father constructor called")

class Mother(Father):
    def __init__(self):
        super().__init__()

        print("Mother constructor called")

class Child(Mother):
    def __init__(self):
        super().__init__()
        print("Child constructor called")

obj = Child()"""


# example of  multiple inheritance:

"""class A:
    variableA="welcome class A"

class B:
    variableB="welcome class B"

class C(A,B):
    variableC="welcome variable C"

C1=C()
print(C1.variableA)
print(C1.variableB)
print(C1.variableC)"""


# create a shape class in which a area method but empty then create a rectangle and circle subclass which implements those formulas and print:
"""import math
class shape():
    def area(self):
        pass

class reactangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        return self.length*self.width
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
     
    def area(self):
        return math.pi*self.radius**2 
    
raect=reactangle(4,5)
print(raect.area())
crcle=circle(5)
print(crcle.area())"""

#multiple inheritence

"""class mother():
    def cook(self):
        print('the mother can cook food ')
    
class father():
    def derive(self):
        print("the father can drive the car")

class child(father,mother):
    def play(self):
        print("the child can play...")

c1=child()
c1.cook()
c1.derive()
c1.play()"""

#find the output of following code:
"""class parent:
    def say_anything(self):
        print("hello form parent class")
    
class child(parent):
     def greet(self):
         print("hii i am Ritik_upadhyay")
    
    
obj=child()
obj.say_anything()"""

    
# multiple inherit with constructor:
"""class teacher:
    def __init__(self):
        print("A teacher can teach:")
        super().__init__()
  
class writer():
    def __init__(self):
        print("A writer can write: ")

class person(teacher,writer):
    def __init__(self):
        super().__init__()
        
        print("A person can both work:")


object=person()"""
# other way:using MRO(METHOD RESOLUTION ORDER..)

"""class teacher:
    def __init__(self):
        print("A teacher can teach:")
  
class writter():
    def __init__(self):
        print("A writer can write: ")

class person(teacher,writter):
    def __init__(self):
        teacher.__init__(self)
        writter.__init__(self)
        
        print("A person can both work:")


object=person()"""





    
    



        
                 



    








    





































