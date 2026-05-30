# print  your name 10 time using for loop:
"""n=1
for i in range(1,11):
    print(i,"Ritik")"""
    


#print the giving list elements uing for loop:

"""list=[1,4,9,16,25,36,49,64,81,100]
for elements in list:
    print(elements)"""


#print these list name using for loop:
"""name=["ritik","ravi","sonna"]
for i in name:
    print(i)"""

#print countig 1 to 100 using for loop:
"""i=1
for counting in range(1,101):
    print(counting)
    i+=1"""

# Guess  output of this  code.....

"""nums=[10,20,30]
for i  in enumerate(nums,start=5):
  print(i)"""


# print reverse counting 100 to 1 using for loop:
"""n=10
for number in range(10,0,-1):
    print(number)"""
    
#print star(*) pateern using for loop:
"""*
**
***
****
*****

for star in range(1,10):
    print("*"*star)"""

# print reverse star pattern using for loop:
"""*****
****
***
**
*"""
"""for  star in range(6,0,-1):
    print("*"*star)"""

   
#print all odd no. using for loop blw 1 to 20:
"""for odd_number in range(1,21,2):
    print(odd_number)"""


# print all even no.blw 0 to 21 using for loop:
"""for even_number in range(0,21,2):
    print(even_number)""" 

# second method :
"""for even_no in range(1,26):
    if(even_no%2==0):
        print(even_no)"""


#check a number is prime or not using for loop:

"""num = int(input("enter a any number!"))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} not a prime no.")
            break
    else:
        print(f"{num} is a prime no.")
else:
    print("not prime")"""


#for loop using else statements:
  
"""for i in range(1,11):
    print(i)
    i==5
else:
    print("it is complete run without break!")"""

"""for i in range(10):
    print(i)
    if(i==5):
     break
else:
    print("now it not execute!")"""

# find the factorial of n number using for loop;
"""n=int(input("enter the number!"))

factorial=1
for i in range(1,n+1):
    factorial*=i
    print(factorial)"""

#find the sum of n natural number using for loop:
"""n=5
sum=0
for i in range(1,6):
    sum+=i
print("The sum of starting five numbers is=",sum) """

#find the any elements using for loop:
"""tuple=(1,4,9,16,25,100,36,49,64,81,100)
x=100
index=0
for i in range(len(tuple)):
    if tuple[i]==x:
        print("elements is find at index",index)
        
    index+=1
else:
        print("searching:")"""


# print any table using for loop:

"""table=int(input("enter any table number:"))
for i in range(1,11):
    print(i*table)"""


# print fabbonacci series using for loop:
"""series=int(input('enter the numbers:'))
a=0
b=1
for i in range(series):
    print(a ,end=",")
    c=a+b
    a=b
    b=c
"""

# print the prime number from 2 to 50 with for loop:
"""print("The prime number series:")
for num in range (2,50):
    is_prime=True
    for number in range(2,num):
        if (num% number==0):
            is_prime=False
            break
    else:
        print(num) """


# find the output of this code:
"""x=0
for i in range(0,5,2):
    x+=i
print("The output is:",x)"""


# find the output of this code:
"""x=1
for i in range (5):
    x*=i
print(x)"""

# find the output of this code:
"""x=[1,2,3,4,5]
for i in x:
    if i==3:
        x.remove(i)
print(x)"""

# find the output of this code:
"""char="hello world"
print(char[::-1][-5:])"""
