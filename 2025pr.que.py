"""class students():
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("welcome!..")

student=students("Ritik_upadhyay..")
student.hello()
print(student.name)"""



"""class students():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def hello(self):
        print(f"hello {self.name} ,your marks is....")


    def get_marks(self):
        print(f"{self.marks}")
    
stu=students("Ritik_upadhyay","90 percentage")
stu.hello()
stu.get_marks()"""



"""class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_average(self):
      sum=0
      for value in self.marks: 
         sum+=value
      print("hello",{self.name},"your marks is",self.marks, "and your average score is",{sum/3},"congratulations!.....")
students=student("Ritik_upadhyay",[50,50,50])
students.get_average()"""


"""class students():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    @property 
    def check_marks(self):
       if(self.marks>=0 and self.marks<100):
           print("yes! teacher you can put the marks")
       else:
           print(" sorry teacher not valid this features.. ")

        
s1=students("Ritik",10)
s1.check_marks"""



"""def method(name):
    def wrapper():
     print("hii")
     name()
     print("welcome")
    return wrapper

@method
def name():
    print("Ritik")
onj=name()"""



""""def method(add):
    def wrapper(a,b):
        print("the value of a",a,"and the value of b is",b)
        sum=a+b
        print("now the finally result is..")
        result=sum
        print(result)
    return wrapper


@method
def add(a,b):
    sum=a+b
    return sum
Sum=add(12,12)"""



"""class car():
  def __init__(self):
    self.acc=False
    self.brake=False
    self.clutch=False


  
  def car_started(self):
    self.acc=True
    self.brake=True

    self.clutch=True
    print("The car is started....")

CAR=car()
CAR.car_started()"""

"""def calculate_area(radius):
    area=3.14*radius*radius
    return area
print("area=",calculate_area(5))"""

"""from turtle import*
speed(0)
bgcolor("green")
colours=["blue"]
hideturtle()
for i in range(122):
    goto(0,0)
    color(colours[i%1])
    forward(130)
    left(5)
    circle(10)
    forward(130)
    right(360)
done()"""

"""age=int(input("enter a number...."))
if age<18:
    raise ValueError ("age must be greater than 18")
else:
    print('you are eligible..')"""


#find the output of the following code:
"""d={"a":1,"b":2}
keys=d.keys()
d["c"]=3
print("c" in keys)"""


# find the output of this code:
"""*x,y=10,20
print(x,y)
"""

 
#find the output of this code:
"""num=2
for number in range(2,2):
    if num%2==0:
        print("success")
    else:
        print("fail..")"""  # no any output of this code..



# write a programm which is change usdt into INR:

"""while(True):
   usdt_value=int(input("enter usdt:"))
   one_usdt=90
   inr_value=usdt_value*90
   print("usdt_value=",inr_value,"INR")"""



#find the output of this code:

"""def f(a,ist=[]):
    ist.append(a)
    return ist
print(f(1),f(2),f(3))"""
 
#find the output of this code:
"""value=3.14159
print(round(value,5))"""


# write a code and add new information in dictionary:
"""dict={"name":"Ritik","age":21}
dict["height"]="5'2"
print(dict)"""

# find the output of this code:
"""d={"x":1}
print(d.get("y",100))"""

    
"""
def find_fact():
    fact = 1
    for num in range(1, 6):
        fact *= num
        print(fact)

find_fact()"""

"""
while(True):
  import math
  factorial1=int(input("enter number:")) 
  new_fact=math.factorial(factorial1)
  print(new_fact)
"""


# def a function which is change feranite to celcius :
"""while(True):
  def change_feranite_into_celcius():
    feranite=float(input("enter the value of feranite for convert into celcius.."))
    celcius=(feranite-32)*5/9
    print(celcius)
  change_feranite_into_celcius()"""
    


# def a function which is change celcius to feranite:

""""def change_celcius_into_feranite():
        celcius=float(input("enter the celcius for convert inti feranite..."))
        feranite=(celcius*9/5)+32
        print(feranite)
change_celcius_into_feranite()"""

#in simple 


"""fehranite=float(input("enter the feranite.."))
celcius=(fehranite-32)*5/9
print("celcius =",celcius,"celcius")"""


"""celcius=float(input("enter the feranite.."))
fehranite=(celcius*9/5)+32
print("fehranite =",fehranite)"""


#check a number prime or not a prime..

"""number =int(input("enter any number..."))
if number < 2:
    print("invalid input..")
else:
    is_prime=True
    for i in range(2,number):
        if number % i==0:
            is_prime=False
            break
    if is_prime:
        print("prime!..")
    else:
        print("not a prime..")
print("Thanks for cheacking...")"""

"""while(True):
   number =int(input("enter any number..."))
   if number <2:
    print("invalid input..")
   else:
    for i in range(2,number):
        if number%i==0:
            print("not prime..")
            break
    else:
        print("prime")"""


"""def check_prime(n):
    if n<2:
        return "invalid input"
    else:
        prime=True
        for i in range(2,n):
            if n%i==0:
                prime=False
                break
        if prime :
            print("prime")
        else:
            print("not a prime..")
result=int(input("enter the number.."))
check_prime(result)"""


# how to check armstorng number..
"""number=int(input('enter the number..'))
save=number
digit=len(str(number))
sum=0
while save>0:
    digits=save%10
    sum=sum+digits**digit
    save=save//10
if sum==number:
    print("the number is armstrong.")
else:
    print("not armstrong..")"""


# what is the ouput of this code:
#print(x:="bob",len(x)) # out of this is bob3:


#f-c
"""
feranite=int(input("enter the feranite value.."))
celcius=(feranite-32 )*5/9
print(celcius)
"""

#c-f
"""celcius=int(input("enter the celcius value.."))
feranite=(celcius*9/5)+32
print(feranite)    """



# check the vowels and character:
"""character=input("enter any character..")
if character in "aeioueAEIOUE":
    print("vowels:")
else:
    print("constant:")"""


# what will be the output of this code:
"""nums=[1,2]
nums.append(nums)
print(nums)
""" 


"""number=10
text="#"
print(number*text)"""



"""name="hello"
name="H"+name[1:]
print(name)"""



# Guess output of this code:
"""def gen():
    yield 10

g=gen()
print(next(g,"DONE"))
print(next(g,"DONE"))"""


"find the output of this code:"
"""exceute=print
exceute("hello,world:")"""


"""find its output:
print(sum([True,True,False]))"""

"""a=[]
a.append(a)
print(a)"""

#  find its output:
"""print(*2*"12",sep="_")"""

#object attribute based questions:

"""class person:
    def __init__(self):
        self.name="Ritik_upadhyay"
        self.age=23

object=person()
object2=person()
object2.name="Sachin"
object2.age=25
print("The person name is:",object.name,"age is:",object.age,"Years:")
print("The person name is:",object2.name,"age is:",object2.age,"Years:")"""

         
# find the output of this code:

"""numbers=[0.5,1.5,2.5,3.5]
print([round(n) for n in numbers])"""

# find the output of this code:

"""list=["A1","B2","C3"]
print(list[-1],[-1],[-1])"""

# you have a list of numbers count only even number from the list:

"""numbers=[1,5,3,9,2,8]
count=0
for num in numbers:
    if num % 2==0:
        count+=1
print(count)"""

# you have a list of string count words longer than 3 characters uing the simple loop:
"""words=["cat","dog","bird","rat","bat"]
count=0
for Words in words:
    if  len(Words)>3:
        count+=1
print(count) """

#you have a list of numbers find the maximum numbers from the list:
"""numbers=[10,20,15,5,25,30]
max_num=numbers[0]
for num in numbers:
    if num > max_num:
        max_num=num
print(max_num)"""


# you have a sales data by months: find the consecutive months where sales are increased (current> perevios):
"""monthly_sales=[
    {"month":"January","sales":100},
    {"month":"february","sales":150},
    {"month":"march","sales":120},
    {"month":"April","sales":180}
]

Result=[]
for i in range(1,len(monthly_sales)):
    previous=monthly_sales[i-1]["sales"]
    current=monthly_sales[i]["sales"]
    if current > previous:
        Result.append(f"{monthly_sales [i-1]["month"]} -> {monthly_sales [i] ["month"]}: {current } >{previous}")

for result in Result:
    print(result)"""


"""# you have employee work hours across multiple days: find the employee who worked more than 20 hours  total across all days:
work_hours=[{""
"emp_name": "Ritik","day":"monday","work_hours":8},
{""
"emp_name": "Ravi","day":"monday","work_hours":6},
{""
"emp_name": "Ritik","day":"Tuesday","work_hours":7},
{""
"emp_name": "Ravi","day":"Wednesday","work_hours":8},
{""
"emp_name": "Ritik","day":"monday","work_hours":8}
]

Total={}
for records in work_hours:
    employee=records["emp_name"]
    hours=records["work_hours"]
    
    if employee in Total:
        Total[employee]+=hours
    else:
        Total[employee]=hours
high_hours=[employee for employee ,hours in Total.items() if hours>20]
print(high_hours)
"""

# find the output of this code:

"""x="123"
y=int(x)
print("The output is:",y+2)"""

# you have a list of tempreature find the first tempreature above 27:
"""tempreature=[23,25,24,28,26,30,22]
for temp in tempreature:
    if temp>27:
        print(temp)
        break
    else:
        pass"""

"""find the output of this code:

moving_average([2,4,6,8],2) 

def moving_average(arr,k):
    result=[]
    for i in range(len(arr) -k+1):
        avg=sum(arr[i:i+k])/k
        result.append(avg)
    return result
print(moving_average([2,4,6,8],2))"""


# you have a text:extract only alphabatic chracter:
"""text="Datascience2026"
character=text[:11]
print(character)"""


#2nd method:
"""text="Datascience2026"
only_albha="".join([char for char in text if char.isalpha()])
print(only_albha)"""


# you have a :extarct only the digits from the string and ignore all chracter or letters:
"""text="Data_Analytics2026"
digit=text[14:]
print(char)"""

#2nd method:
"""text="Data_Analytics2026"
digit="".join([num for  num in text if num.isdigit()])
print(digit)"""


# you have a list of numbers use list comperihension and create a new list  with square of even numbers:

"""numbers=[1,5,2,8,3,7]
square_of_num=[x**2 for x in numbers if x %2==0]
print(square_of_num)"""       
        
# you have data in list use list comperihesnion to create a new list with only numbers greater then 15 multipliy by 2:

"""data=[10,25,5,30,15,20]
new_list=[x*2 for x in data if x>15 ]
print(new_list)
"""


# Input Dictionary Use dictionary comprehension to create a new dict with only quarters having sales > 20,000.

"""sales = {'Q1': 15000, 'Q2': 23000, 'Q3': 18000, 'Q4': 27000}
high_quantity={k:v for k,v in sales.items() if v>20000}
print(high_quantity)"""

# Find the output of this code:
"""a=[1,2]
b=a
b[0]=99
print(a)"""


# Find the output of this code:
"""print(""==False)"""


# find the outputof this code:

"""a=[1,2]
b=list(a)
c=a
print(a == b)
print(a is b)
print(a is c)"""


# what wiil be the output of this code:
"""for i in range (3):
    print(i)
    continue
    print("x")"""

# what wiil be the output of this code:
"""d={"a":1, "b": 2}
d["c"]=d.get("a")+d.get("b")
d["a"]=10
print(d)"""

"""find the output:
print("5"+"6"*2)"""

# find the output:
"""a=8
b=2
a=a*b+3
b=a//4
a=a%b
print(a+b)"""
  