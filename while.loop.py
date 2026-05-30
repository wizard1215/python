# while loop is work repeatdley until the certain condition is true:
#print counting from 1 to 10:
"""i=1
while i<=10:
    print(i)
    i+=1"""

"""name=1
while name<=20:
    print(name,"Ritik _upadhyay")
    name+=1"""

#print 13 table using while loop:
"""i=1
while i<=10:
    print(i*13)
    i+=1"""

#print any table according to user:
"""table=int(input("enter the number:"))
i=1
while i<=10:
    print(i*table)
    i+=1"""

# reverse counting 100 to 1 :
"""i=100
while i>=1:
    print(i)
    i-=1"""



#find factorial of 7:
"""num=7
i=1
factorial=1
while i<=num:
    factorial*=i
    print(factorial)
    i+=1"""


#find the factorial according to user:
"""number=int(input("enter the number:"))
i=1
factorial=1
while i<=number:
    factorial*=i
    print(factorial)
    i+=1"""


"""print the elements of this list using while loop:
the given list as:"""

"""list=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(list):
    print(list[index])
    index+=1"""


#print the fruits in using while loop:
"""fruits=["mango","apple","papayaya","littchi","pear","banana"]
index=0"""
"""index=len(fruits)-1
print(index)
while index<len(fruits):
    print(fruits[index])
    index+=1"""

# search any number from this tuple using while loop:
 
"""elements=(1,4,9,16,25,36,49,64,81,100,36,12,13,36)
x=36
index=0
while index < len(elements):
 if(elements[index]==x):
  print("x is found at index",index)
 else:
  print("try to find")
 index+=1"""

# using break statements :
"""i=0
while i<=20:
    print(i)
    if(i==11):
        break  
    i+=1"""
    
"""elements=(1,4,9,16,25,36,49,64,81,100,36,12,13,36)
x=36
index=0
while index < len(elements):
    if(elements[index]==x):
        print(" x is found at index",index)
        break
    else:
        print("try to find:")
    index+=1"""

# use of continue statements:
"""i=1
while i<=10:
    if(i==3):
        i+=1
        continue
        
    print(i)
    i+=1"""


# print all even no.blw 1 to 20:using while loop:
"""i=0
while i<=20:
    print(i)
    i+=2"""


# print all odd no.blw 1 to 20:

"""i=1
while i<=20:
    print(i)
    i+=2"""

#print all prime no.blw 1 to 100: using while loop:
"""n=2
while n<100:
    is_prime=True
    i=2
    while i*i<=n:
        if(n%i==0): 
            is_prime=False
            break
        i+=1
    if(is_prime):
        print(n)
    n+=1"""
# cheack prime number with using import module:
"""import math
number=int(input("enter the numbers:"))
if number<2:
    print("not prime:")
i=2
is_prime=True
while i<=math.sqrt(number):
    if number%i==0:
        is_prime=False
        break
    i+=1

if is_prime:
    print("prime:")
else:
    print("not a prime:")"""


#second method
"""user_enter =int(input("enter any number"))
i=2
is_prime=True
while i<user_enter:
    if(user_enter%i==0):
        is_prime=False
        break
    i+=1
print(f"prime:{is_prime}")"""

"""#third method:
n=int(input("enter any numbers!:"))
i=2
while i<n:
    if(n%i==0):
        print("not prime!:")
        break
    i+=1
else:
    print("yes prime!:")"""



"""print a star(*) pattern using while loop:
*
**
***
****
***** """

"""i=1
while i<=5:
    print("*" *i)
    i+=1"""

# 2nd method:
"""i=1
while i<=5:
    j=1
    while j<=i:
     print("*" ,end="")
     j+=1

    print()
    i+=1"""

"""print the star pattern in reverse
*****
****
***
**
**"""


"""i=5
while i>=1:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i-=1"""


"""i=5
while i>=1:
    print("*" *i)
    i-=1  """  


# find the factorial without using any specific method:
"""import math
factorial=math.factorial(7)
print(factorial)"""
 

# find the sum of n natural number:

"""n=int(input("enter numbers!"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("sum of numbers",sum)"""

#fail questioon 
"""n=int(input("enter any number!:"))
if(n<2):
    print("not prime!")
elif(n==2 or n==3):
    print("prime!")
elif(n%2==0 or n%3==0):
    print("not prime!")
else:
    print("prime")"""


# print fabbonacci series using while loop:
"""num=int(input("enter the numbers:"))
a=0
b=1
c=0
count=0
while count<num:
    print(c,end=",")
    c=a+b
    a=b
    b=c
    count+=1"""

# find the output of this code:
"""i=1
while i<4:
    print(i)
    i*=2"""









  



























