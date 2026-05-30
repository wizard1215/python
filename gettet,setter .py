# example of getter method:

"""class person:
    def __init__(self,first_name,last_name):
        self.__first_name=first_name
        self.__last_name=last_name

    def get_full_name(self): #getter_method
        print(f"{self.__first_name} {self.__last_name}")
    
person1=person("Ritik","upadhyay!")
person1.get_full_name()"""


# setter method:
# example of setter method:

"""class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):  # Setter method
        if isinstance(name, str):
            self._name = name 
        else:
            raise ValueError("Name must be a string")

person = Person("Alice")
person.set_name("Bob")
print(person.get_name()) """

# important in setter method if givin condition is fail then old value not upadte :for update value give passig condition
"""class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_name(self):
        print("The person name is:",self.name)


    def set_age(self,new_age):
        if new_age>1 and new_age <101:
            self.age=new_age
        else:
            print("invalid age:")
object=person("Ritik",21)
object.get_name()
object.set_age(-4)
print(object.age)"""
 
""""class students:
    def __init__(self,name):
        self.name=name
        self.marks=None

    def set_marks(self,new_marks):
        if new_marks >=0 and new_marks <101:
            self.marks=new_marks
        else:
            new_marks=None
            print("invalid input:")

    def get_info(self):
        print("The students name is:",self.name)
        if self.marks is not None:
            print("The students marks is:",self.marks)
        else:
        
         print("you enter wrong input:")

s1=students("Ritik")
s1.set_marks(900)
s1.get_info()"""
"""
class person:
    def __init__(self,name):
        self.name=name
        self.age=None
    
    def set_age(self,new_age):
        if new_age>0 and new_age<101:
            self.age=new_age
        else:
            print('invalid age :')

    def get_info(self):
        print("The students name is:",self.name)
        if self.age is not None:
         print("The sudents age is:",self.age)
        else:
            print("you enter wrong input:")
s1=person("Ritik")
s1.set_age(25)
s1.get_info()"""








































