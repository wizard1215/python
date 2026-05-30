# methods are the functions which is belongs in the objects:
"""class students:
    def __init__(self,name):
        self.name=name
    
    def hello(self):
        print(f"hello,{self.name}")

Students=students("Ritik_upadhyay!")
Students.hello()"""
       

"""class students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def _hello(self):
        print(f"welcome,{self.name}")

    def get_marks(self):
        print(f"hello,{self.name},yours marks is,{self.marks}")

Students=students("Ritik_upadhyay",65)
Students.get_marks()"""
    
    
    
"""class cat:
    def __init__(self,name):
        self.name=name
    
    def Cat (self):
        print(f"{self.name}")

    def said(self):
        print(f"{self.name},says myau!")
CAT1=cat("cat")
CAT1.said()"""


"""class dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(f"{self.name},says woof!")

Dog=dog("Jimmy")
Dog.bark()"""

 
# To create a students class take the students name and number of three subject and print average:

"""class students:
   
     def __init__(self,name,marks):
        self.name=name
        self.marks=marks
     def get_average(self):
        sum=0
        for value in self.marks:
            sum+=value
        print(f"hii,{self.name},your marks is ,{self.marks},and your average score is",sum/3)
Students=students("Ritik_upadhyay",[10,10,10])
Students.get_average()"""


"""#convet fahrenheit to celsius: 

class tempreature():
    @staticmethod
    def celsius(fahrenheit):
        return (fahrenheit-32)*5/9
#print(fahrenheit.celsius(98.6)) 
object=tempreature()
print(tempreature.celsius(98.6))"""
                  

"""
a=2
b=3
print(pow(a,b))"""


#decorator based questions:
"""def personal_fnc(get):
    def wrapper():
        print("welcome..")
         
        get()
        print("thanks..")
    return wrapper
@personal_fnc
def get():
    print("Hello Ritik_upadhyay....")
 
get()"""

"""def add_smart(addition):
    def wrapper(a,b):
        print("the value of a is",a,"and the value of b is",b,"and the sum a of and b is=")
        result=addition(a,b)
        print("Result=",result)
      
       
    return wrapper

@add_smart
def addition(a,b):
    return(a+b)
addition(13,12)"""


"""
def repeat_three_times(hello):
    def wrapper():
        print()"""

"""def repeat_three_times(greet):
    def wrapper():
        for function in range(3):
         greet()
    return wrapper



@repeat_three_times
def greet():
    print("hii")
greet()"""


#wrd which is give only even number square if number is odd its no valid....

"""def only_even(show_sqre):
       def wrapper(n):
            if(n%2==0):
              show_sqre(n)
            else:
                 print("odd number squre is not valid..")
       return wrapper 
@only_even
def show_sqre(n):
    print(n**2)
show_sqre(8)"""


#make a decorator @uppercase the converts any string return by a function into uppercase:

"""def uppercase(msg):
    def wrapper():
        return msg().upper()
        msg()
    return wrapper

@uppercase
def msg():
    return "ravi"
m1=msg().upper()
print(m1)"""

"""def complete_divide(divide):
    def wrapper(n):
        if(n%2==0):
            return divide(n)
        else:
            print("this feature not valid..")
    return wrapper
@complete_divide
def divide(n):
    divide1=n//2
    print("zero")
divide(9)"""


"""class students():
    college_name="diet"
    def __init__(self,name):
        self.name=name
s1=students("ritik")
s2=students('tushar')
s3=students("sonna")
print(s1.name,s1.college_name)
print(s2.name,s2.college_name)
print(s3.name,s3.college_name)"""

"""nums=[10,20,30]
for i  in enumerate(nums,start=5):
  print(i)"""













        












     
    
    











