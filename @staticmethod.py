# classmethod is a decorator in python which is used only the class data(attribute,property)
#and use the (cls) variable as:

"""class students:
    school_name="DIET"
    @classmethod
    def show_school_name(cls):
        print("The students school name:",cls.school_name)
s1=students.show_school_name()"""


"""class car:
    wheel=4
    @classmethod
    def cheack_wheel(cls):
        print("The car have wheel:",cls.wheel)
car.cheack_wheel()"""


"""class company:
    company_name="TCS"
    
    @classmethod
    def change_company(cls,name):
        cls.company_name=name
   
print("The old company name is:",company.company_name)
company.change_company("Infosiys:")
print("Now the new company name is:",company.company_name)"""


"""class students:
    count=0

    def __init__(self,name):
     self.name=name        
     students.count+=1
    
    @classmethod
    def total_students(cls):
       print("The tottal sudents is:",cls.count)

s1=students("Ritik")
s2=students("Ravi")
s3=students("Rahul")   
s4=students("viraj")
s5=students("aanchal")
students.total_students()"""


"""class bank:
    bank_name="SBI"
    
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name=name

print("The old bank name is:",bank.bank_name)
bank.change_bank_name("HDFC")

print("Now the new bank name is:",bank.bank_name)"""


"""class book:
    category="EDUCATION"
    
    @classmethod
    def show_category(cls):
        print("The book category is:",cls.category)
book.show_category()"""

# Guess the its output:
"""class Test:

    x = 10

    @classmethod
    def show(cls):
        print(cls.x)

Test.show()"""

# Guess the its output:

"""class Demo:

    x = 5

    @classmethod
    def change(cls):
        cls.x = 20

Demo.change()
print(Demo.x)"""

# Guess the its output:
"""class A:

    x = 100

    @classmethod
    def show(cls):
        cls.x = 200

A.show()
print(A.x)"""

# wap to change old  discount with new discount: 
"""class product:
    discount="10 %"

    @classmethod
    def change_discount(cls,change):
        cls.discount=change

    
print("old discount is:",product.discount)
product.change_discount("20%")
print("now new discount is:",product.discount)"""

# second type for changing the classsmethd:

"""class person:
    person_name="Ritik_uapdhyay"
    @classmethod
    def show_name(cls):
        print("The old name is:",cls.person_name)
    @classmethod
    def change_name(cls,new_name):
        cls.person_name=new_name
person.show_name()
person.change_name("Ravi_upadhyay")
print("now the new name is:",person.person_name)"""

"""class percent:
    percentage="10%"
    @classmethod
    def show_percent(cls):
        print("the old percentage is:",cls.percentage)

    @classmethod
    def change_percent(cls,new_percentage):
        cls.percentage=new_percentage
    
percent.show_percent()
percent.change_percent("20%")
print("The new percent is",percent.percentage)"""

#static method  is method which is define in the class but it is not realated to the class instance:
# we can call to staticmethod with class name and instance or object through: 

"""class math:
    @staticmethod
    def add(a,b):
        return a+b
print(math.add(2,5))#class name use krke
object=math()
print(object.add(2,4))"""#instance ka use karke


"""class person:
    @staticmethod
    def person_name():
        name="ritik"
        print(name)
person.person_name()#class name use krke
object=person()
object.person_name()#instance ka use karke"""


"""class car:
    @staticmethod
    def car_name():
        name="scorpio"
        print(name)
car.car_name()
object=car()
object.car_name()"""
        


"""class math:
    @staticmethod
    def diff(a,b):
        return(a-b)
print(math.diff(10,20))
math1=math()
print(math1.diff(20,5))"""






































#instance method:the instance method is call only object name use self parametre:

"""class students:
    def __init__(self,name):
        self.name=name
    def stu_name(self):
        print("The students name=",self.name)

s1=students("ritik")
s1.stu_name
print(s1.stu_name())"""













    


