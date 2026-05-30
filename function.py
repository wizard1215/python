#function is a block of statements which is peform any spacific task are called function:

"""def print_hello():
 
 print("hello_world!")

print_hello()"""

"""def print_name():
    print("Ritik_upadhyay!")
print_name()"""


#add two no.using function:
"""def sum_cal(a,b):
    sum=a+b
    return sum
addition=sum_cal(12,12)
print(addition)"""

#add three no.using function:

"""def sum_cal(a,b,c):
    sum=a+b+c
    return sum
addition=sum_cal(10,20,20)
print(addition)"""

#calculate diffrence blw to number using function:
"""def cal_diff(a,b):
    diff=a-b
    return diff
subtract=cal_diff(10,5)
print(subtract)"""

#calculate multiplicataion of two using function:

"""def cal_mul(a,b):
    mul=a*b
    return mul
multiplication=cal_mul(12,5)
print(multiplication)"""


# calculate divission of two number using function:
"""def div_cal(a,b):
    div=a%b
    return div
division=div_cal(12,5)
print(division)"""


# find the averag of three number using function:
"""def cal_average(a,b,c):
    sum=a+b+c
    average =sum/3
    return average
Average=cal_average(10,10,10)
print(Average)"""

# default parametre :
"""def find_product(a ,b=5):
    product=a*b
    return product
pro=find_product(10)
print(pro)"""


# practice questions on functions:

#wap programme to print the len of list which is given as:

"""names=["Ritik","ravi","sonna","shiv","pari"]
actors=["srk","akshyay kumar","salman khan","sunny deol"]
countries=["india","bhopal","japan","belgium","china"]
mobiles=["Redmi","Realme","oppo","samsung"]
def print_len(list):
    print(len(list))
print_len(names)
print_len(actors)
print_len(countries)
print_len(mobiles)"""


# print the elements of a list in a single line using function:
"""countries=["india","japan","nepal","china","belgium","aferica"]
def print_elemetns(countries):
    for item in countries:
        print(item,end=",")
print_elemetns(countries)"""
    

"""names=["Ritik","ravi","sonna","shiv","pari"]
def print_elements(names):
    for i in names:
        print(i,end=",")
print_elements(names)"""


#find the  factorial of n using function,where n is 5 :

"""def cal_fact(factorial):
    factorial=1
    for i in range(1,6):
        factorial*=i
        print(factorial)
cal_fact(5)"""


# covnert USDT TO INR:

"""def money_converter(USdT_value):
   
   inr_value=USdT_value*87.67
   print(inr_value,"INR=",USdT_value,"USDT")
money_converter(100)"""


"""names=["ritik","sonna","ravi"]
def find_name():

 for elements in names:
 
    print(elements,end="\n")
find_name()"""

# find the output of this code:
"""def function(x):
    x=x+10
a=5
function(a)
print(a)"""


# what is output of this code:
"""def check(n):
    if n>0:
        return "positive"
    pass
print(check(-1))"""


# what is printed:
"""def cal(a,b=5):
    return a*b
print(cal(2,3))"""


# what is printed:
"""def test():
    return 
print(test())"""

# what is printed:
"""def add(a,b):
    print(a+b)
result=add(2,3)
print(result)"""

# def a function which is change usdt value into INR:
"""while(True):
   def change_money(INR):
    return INR
   usdt_value=int(input("enter usdt..."))
   print("usdt_value=",usdt_value*90,'INR')
   change_money(usdt_value)"""




