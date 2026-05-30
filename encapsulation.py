# encapsulation is a second pole in opps which is wrapping to data and then after access with using getter and setter method and another method:

"""class employee:
    def __init__(self,name,salary):
        self.__salary=salary
        self.name=name

    def get(self):
        return self.__salary
    
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary!")

Employee=employee("Ritik_upadhyay",15000)
print(Employee.name)
print(Employee.get())
Employee.set_salary(5000)
print(Employee.get())"""


"""class account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get(self):
        return self.__balance
    
    def show_balance(self,balance):
        if(balance>0):
            self.__balance=balance
        else:
            print("invalid balance in your account!")
Account=account("Ritik_upadhyay",10000)
print(Account.name)
print(Account.get())
Account.show_balance(0)
print(Account.get())"""


"""class information:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_age(self):
        self.__age
        return self.__age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name

    def set_age(self,age):
        self.__age=age

Information=information("ritik",20)
Information.get_name()
Information.get_age()
print(f"The name is ,{Information.get_name()},and the age is {Information.get_age()} years old")"""



"""class bankAccount():
    def __init__(self,balance):
        self.__balance=balance


    @property
    def check_balance(self):
        print("Balance is",self.__balance)


    def deposit_balance(self,amount):
        if self.__balance>0:
            self.__balance+=amount
            print("deposited balance is",amount)
            print("now your balance is",self.__balance)

          
    def withdrawl(self,amount):
        if 0<self.__balance >amount:
            self.__balance-=amount
            print("withdrawl balance is",amount)
            print("Remanining balance is your account is",self.__balance)
        else:
            print("insufficent balance..")
account=bankAccount(1000)
account.check_balance
account.deposit_balance(500)
account.withdrawl(600)"""

"""
class students:
    def __init__(self,name,marks):
        self.name=name
        self.set_marks(marks)

    def set_marks(self,new_marks):
        if new_marks>0 and new_marks<=100:
            self.marks=new_marks
        else:
            print("invalid marks:")
            self.marks=0
    
    def get_info(self):
        print("the students name is:",self.name)
        print("the students marks is:",self.marks)


s1=students("Ritik",-4)
s1.get_info()"""


"""class person:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,new_marks):
        if new_marks >0 and new_marks <2000:
         self.__marks=new_marks
            
        else:
            print("invalid input:")
p1=person("Ritik",20)
print(p1.name)
p1.set_marks(-22)
print(p1.get_marks())"""


        



    






 


      





























"""class Students:
    def __init__(self, name, marks):
        self.name = name
        self.set_marks(marks)  

    def set_marks(self, new_marks):
        if new_marks > 0:
            self.marks = new_marks
        else:
            print("invalid marks:")
            self.marks = None  

    def get_info(self):
        print("the student's name is", self.name)
        if self.marks is not None:
            print("the student's marks is", self.marks)
        else:
            print("marks not set due to invalid input")

s1=Students("Ritik",-6)
s1.get_info()"""
















   










        


       
   





  
    
    




   



















