#find the square of the numbers using def function with map function

"""def square(nums):
    return nums*nums

numbers=[2,3,4,5,6]
print(tuple(map(square,numbers)))"""

#find the double of the numbers using def function with map function

"""def double(nums):
    return nums*2

numbers=[2,3,4,6,8,9,10,12,16]
print(set(map(double,numbers)))"""

# converting upper  case letter
"""name=["ritik","ravi","sonna","pari"]
result=(tuple(map(str.upper,name)))
print(result)"""

# map function with lambda:
"""a=[3,4,5,6,7]
b=[6,7,2,10,6]
result=(list(map(lambda x,y: x+y,a,b)))
print(result)"""

"""nums=[2,3,4,6]
nums1=[3,4,5,8]
result=(set(map(lambda a,b:a+b,nums ,nums1)))
print(result)"""

# map with builtein function
"""data=["2","3","5","7","8","9"]
result=map(int,data)
print(list(result))"""


# map function with condition:
"""nums=[1,2,3,4,5,6,7,8,9,10,11,21,12,13,15,20]
result=(tuple(map(lambda x:"Even" if x%2==0 else "odd",nums)))
print(result)"""


# filter select only True elements :

"""numbers=[2,12,3,5,6,77,88,22,23,212,34,67,886,10,9000,9776,3445,]
if numbers>10:
    print('TRUE')
else:
    print("False")

print(list(filter(lambda x: x,numbers)))"""

# find the output of this code::

"""I=[1,0,0,2,'hi',',',[]]
print(list(filter(bool,I)))"""


# Wap to find the number whichis the greater than 10: uisng filter:

"""def greater_than(n):
    return n>10
nums=[12,321,45,2,7,812,90,60]
print(tuple(filter(greater_than,nums)))"""

# find only even numbers using filter and find the square using map :

"""def is_even(n):
    return n%2==0
def square(num):
    return num*num
numbers=[12,11,5,6,4,8,10]
result=(map(square,filter(is_even,numbers)))
print(list(result))"""


# write a programme sing with map and filter suppose you have list of names you taking only those name with using filter  having lenth greatre than 4 
# and convert those in upper case lettre..
"""def find_len (name):
    return len(name)>4

def convert_upper_case(names):
    return names.upper()
names=["ritik","ravinder","sonna","ram","sita","nikhile","sunil","om"]
result=map(convert_upper_case,filter(find_len,names))
print(list(result))"""

# you have list of numbers filter only even numbers using map :
"""numbers=[1,2,3,4,5,6,8,9,10]
new_list=map(lambda x: x  if x%2==0 else None,numbers)
print(list(new_list))"""







