# abstraction is a pole of opps in which hide the unncessary detail only show necessary part of function:
"""class car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False
    
    def car_start(self):
        self.acc=True
        self.brake=False
        self.clutch=False
        print("car is start!")
CAR=car()
CAR.car_start()"""



"""class students:
    def __init__(self):
        self.name=False
        self.time=False
        
    def student_percentage(self):
        self.name=True
        self.time=True
        print("students is pass with best percentage!")
Students=students()
Students.student_percentage()"""




"""def calculate_area(radius):
    area=3.14*radius*radius
    return area
print("area=",calculate_area(5))"""


# using with advanced level as..
#form abc import ABC,abstractmethod
"""from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class creditcardpayments(payment):
    def pay(self,amount):
        print("paying",{amount},"Rupess using credit card...")

class phonpaypayments(payment):
    def pay(self,amount):
        print("paying RS",{amount},"using phone pay")

money=creditcardpayments()
money1=phonpaypayments()
money.pay(2000)
money1.pay(3000)"""

"""from abc import ABC,abstractmethod

class animals(ABC):
  @abstractmethod
  def animals_voice():
    pass
  
class voice():
  def cat_voice(animals):
    print("the cat voice is=myau,myau")

class bark()
  def dog_voice(voice):
    print("the dog voice is= woof,woof")

Animal=voice()
Animal1=bark()
Animal.cat_voice()
Animal1.dog_voice()"""

"""from abc import ABC,abstractmethod
class vechile(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class car(vechile):
    def start_engine(self):
        print("The car start:ghau,ghau:")

class bike(vechile):
    def start_engine(self):
        print("The bike start:dhru,dhrun:")

c1=car()
c1.start_engine()
b=bike()
b.start_engine()"""

"""from abc import ABC ,abstractmethod
class payment(ABC):
    @abstractmethod
    def payment_mode(self):
        pass

class phonpay(payment):
    def payment_mode(self):
        print("i pay money with using")"""




"""class students:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

     #@gettermethod
    def get_marks(self):
        return self.__marks

      #settermethod
    def set_marks(self,newmarks):
      if 0<=newmarks and newmarks  <=100:
          self.__marks=newmarks
          print(self.__marks," is valid marks")

      else:
          print("invalid marks")

obj=students("Ritik_upadhyay",90)
print(obj.name),
print("old marks",obj.get_marks())
obj.set_marks(-9)"""


"""from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdrawl(self,amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


    @abstractmethod
    def get_balance(self):
        pass


    @abstractmethod
    def deposit(self,amount):
        pass

class myatm(ATM):
    def __init__(self,balance):
        self.balance=balance


    def get_balance(self):
        print("your current balance is",self.balance)

    def deposit(self,amount):
        self.balance += amount
        print("your deposit balance is",amount)

    def withdrawl(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print("withdrawal transaction",amount)
        else:
            print("insufficent balance....")
    def check_balance(self):
        print("now your Remaining balance is balance is:",self.balance)

atm=myatm(3000)
atm.get_balance()
atm.deposit(300)
atm.check_balance()   
atm.withdrawl(600)   
atm.check_balance()  """


"""from abc import ABC ,abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass

class ractangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
   
    def area(self):
        area_of_ractangle=self.length*self.breadth
        return area_of_ractangle
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        area_of_circle=3.14*self.radius**2
        return area_of_circle
object=ractangle(2,3)
print("The area of ractangle is:",object.area())
object1=circle(5)
print("The area of circle is:",object1.area())"""







    


   
    















    


