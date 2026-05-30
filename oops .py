"""class students:
    name="Ritik_upadhyay"
    standard="B.tech"
    Roll_no=2204980100046
    Branch="computer_science"
Students=students()
print("students name is=",Students.name)
print("students standrd is.=",Students.standard)
print("students roll_no.is=",Students.Roll_no)
print("students branch is=",Students.Branch)"""


"""class car:
    name="scorpio"
    model=2012
    colour="Black"
    engine="Self start"
CAR=car()
print("The car name is=",CAR.name)
print("The car model is=",CAR.model)
print("The car colour is =",CAR.colour)
print("The car engine is =",CAR.engine)"""



# costructor __init__!:
"""class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    print("add new students in database!")
S1=students("Ritik_upadhyay",21)
print("The students name is=",S1.name,"and age is",S1.age,"years")
S2=students("Ravi_tomar",20)
print("The students name is=",S2.name,"and age is",S2.age,"years")
S3=students('Suraj_kumar',16)
print("The students name is=",S3.name,"and age is",S3.age,"years")
S4=students("Nikhile_tomar",15)
print("The students name is=",S4.name,"and age is",S4.age,"years")"""


# wap a programme to create a different variety of mobile phone using oops :
"""class mobile:

    def __init__(self,name,model,Ram):
        self.name=name
        self.model=model
        self.Ram=Ram
    print("add new mobile in database!")
mob1=mobile("Redmi",2020,464)
print("the mobile name is=" ,mob1.name,"the model is",mob1.model,"and the Ram of mobile is",mob1.Ram)
mob2=mobile('OPPO',2020,6128)
print("the mobile name is=" ,mob2.name,"the model is",mob2.model,"and the Ram of mobile is",mob2.Ram)
mob3=mobile("samsung",2010,512)
print("the mobile name is=" ,mob3.name,"the model is",mob3.model,"and the Ram of mobile is",mob3.Ram)
mob4=mobile("nokia",2000,10)
print("the mobile name is=" ,mob4.name,"the model is",mob4.model,"and the Ram of mobile is",mob4.Ram)
mob5=mobile("real mee",2025,512)
print("the mobile name is=" ,mob5.name,"the model is",mob5.model,"and the Ram of mobile is",mob5.Ram)"""

# wap to add new students with their name subeject and marks:

"""class learner:

    def __init__(self,name,subjects,marks):
        self.name=name
        self.marks=marks
        self.subjects=subjects
    print("add new students in database!")
name1=learner("RITIK_UPADHYAY","python",60)
print("The 1st students name is=",name1.name,"the subjects is:",name1.subjects,"and the marks in subjects is:",name1.marks)
name2=learner("Tushar_mittal","java",55)
print("The 2nd students name is=",name2.name,"the subjects is:",name2.subjects,"and the marks in subjcts is:",name2.marks)
name3=learner("Reshu_Thakur","c++",45)
print("The 3rd students name is=",name3.name,"the subjects is:",name3.subjects,"and the marks in subjcts is:",name3.marks)
name4=learner("Anshika_varma","math",45)
print("The 4th students name is=",name4.name,"the subjects is:",name4.subjects,"and the marks in subjcts is:",name4.marks)
name5=learner("Monika_gupta","Data_structure",56)
print("The 5th students name is=",name5.name,"the subjects is:",name5.subjects,"and the marks in subjcts is:",name5.marks)"""


# There are two type of attribute in python which is as:
# class attribute

"""class students:

    college_name="diet"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
Students1=students("Ritik_upadhyay",90)
Students2=students("Ravi_tomar",60)
print("The college name is",students.college_name)
print(Students1.name,Students1.marks)
print(Students2.name,Students2.marks)"""

"""class car:
    wheel="four_wheel"
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
CAR=car.wheel
CAR1=car("scorpio","black")
CAR2=car("maruti","white")
print(car.wheel)
print(CAR1.name,CAR1.colour)
print(CAR2.name,CAR2.colour)"""

#object atttribute!:

"""class students():
    def __init__(self,name,age):
        self.name=name
        self.age=age
students1=students("Ritik_upadhyay!",21)
students2=students("vipin_tomar!",19)
print(students1.name,students1.age,"years")   
print(students2.name,students2.age,"years")"""

"""class mobile:
    def __init__(self,name,Ram):
        self.name=name
        self.Ram=Ram
MOBILE1=mobile("redmi note 7 pro!",464)
MOBILE2=mobile("samsung",828)
print("The mobile name is=",MOBILE1.name,"and mobile Ram is",MOBILE1.Ram)
print("The mobile nam is :=",MOBILE2.name,"and rhe mobile ram is:=",MOBILE2.Ram)"""



"""class students():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    print("add new students in database with their name and age...")

s1=students("ritik",21)
print(s1.name,s1.age)
s2=students("ravi",22)
print(s2.name,s2.age)
s3=students("sonna",11)
print(s3.name,s3.age)"""


"""class college():
    college_name="diet"
s1=college()
s2=college()
print(s1.college_name)
print(s2.college_name)"""

"""class college():
        college_name="diet"

stu1=college()
stu2=college()
stu3=college()
print(stu1.college_name)
print(stu2.college_name)
print(stu3.college_name)"""



"""def function(get_name):
    def wrapper():
        print("welcome")
        get_name()
        print("thnaks")
    return wrapper
@function
def get_name():
    print("hello ritik")

get_name()"""

# based questions on class attribute:
"""class college():
    college_name="DIET"
    def __init__(self,name):
        self.name=name
s1=college("RITIK")
s2=college("TUSHAR MITTAL")
s3=college('RESHU THAKUR')
print(s1.college_name)
print(s2.college_name)
print(s3.college_name)"""


# object attribute based questions:

"""class students:
    pass
s1=students
s1.name="Ritik"
s1.age=21
print(s1.name)
print(s1.age)"""


# who having the high precedence blw object and class attribute and why give an exeample:
"""class college:
    college_name="DIET"
s1=college()
s1.college_name="MIET"
print(s1.college_name)"""
    

# class ,object and instance attribute mixed questions:
       
"""class students:
    collge_name="DIET"
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    
    def show_details(self):
        print("The students name is:",self.name)
        print("The students age is:",self.age)
        print("The students course is:",self.course)
        print("The college name is:",students.collge_name)
s1=students("Ritik",22,"B.tech")
s1.show_details()
s1.city='meerut'
print("city:",s1.city)"""


# find the output of this code:
"""class A :
  def show(self):
    print("A")

class B(A):
  def show(self):
    print("b")
object=B()
object.show()"""











 



































