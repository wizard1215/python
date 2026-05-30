"""class account:
    def __init__(self,account,balance):
        self.account_no=account
        self.balance=balance


    def debit(self,amount):
        self.balance -=amount
        print(f"Rs {amount} ,is debit your account")
        print("now the tottal balance in your account =",self.show_balance())


    def credit(self,amount):
        self.balance +=amount
        print(f"Rs {amount},is credit you !")
        print("now the tottal balance in your account is =", self.show_balance())


    def show_balance(self):
        return self.balance

Account=account(50526616442,10000)
print("The your account no is =",Account.account_no)
print("The balance in your account =",Account.balance)
Account.debit(3000)
Account.credit(5000)"""

"""define a circle class to create a circle with radius using the construtor:
define an area method of class which is calclate area of the circle:
define a perimeter method of class which is allow to calulate the perametre of the circle"""


"""class circle:
    def __init__(self,radius):
        self.radius =radius
    
    def area(self):
        return (22/7)*self.radius**2
    
    def perimeter(self):
        return 2*(22/7)*self.radius
        

c1=circle(21)
c1.area()
print(c1.perimeter())"""



"""define a employee class with attribute role,department,and salary this class show details 
create a engineer class that is inherit the properties from the employees and additional attribute name and age"""


"""class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary


    def show_detail(self):
        print("role=",self.role)
        print("the department=",self.department)
        print("the salary=",self.salary)


class Engineer(employee):
    def __init__(self,name,age):
        super().__init__("data scientist","it","50000")     
        self.name=name
        self.age=age
        
engin=Engineer("Ritik_upadhyay!",21)
engin.show_detail()"""



""" create a class of order which is store the itme and their price using the dunter function __gt__:
to convey that :
order1>order2,if the price of order 1 is greater than order2"""


"""class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(order1,order2):
        return order1.price>order2.price


ord1=order("chips",20)
ord2=order("sugar",10)
print(ord1>ord2)"""

























  



   
   
    