#functions  of list
#1.append()
"""my_list=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,364,400]
orignal_list=my_list.append(441)
print(my_list)"""

#2 .extend()
"""my_list=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,364,400]
my_list.extend([441,484,529])
print(my_list)"""

#3.reverse()
"""my_list=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,364,400]
my_list.reverse()
print(my_list)"""

#4.count()
"""my_list=[1,4,9,16,25,36,49,64,81,100,121,144,169,4,4,196,225,256,289,324,364,400]
count=my_list.count(4)
print(count)"""

#5.insert()
"""my_list=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,364,400]
my_list.insert(1,5)
print(my_list)"""

#6.clear()
"""my_list=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,364,400]
orignal_list=my_list.clear()
print(my_list)
"""
#7.index()
"""my_list=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,364,400]
my_orignal_list=my_list.index(25)
print(my_orignal_list)"""

#8.sort()
"""my_list=[400,364,324,289,256,225,196,169,144,121,100,81,64,49,36,25,16,9,4,1]
my_orignal_list=my_list.sort()
print(my_list)"""

#9.list.sort(reverse=True)
"""my_list=[1,4,9,16,25,36,49,64,81,100,110,144,169,196,225,256,289,324,364,400]
my_orignal_list=my_list.sort(reverse=True)
print(my_list)"""

#10.remove()
"""my_list=[1,4,9,16,25,36,49,64,81,100,110,144,169,196,225,256,289,324,364,400]
my_orignal_list=my_list.remove(25)
print(my_list)"""

#11.pop()
"""my_list=[1,4,9,16,25,36,49,64,81,100,110,144,169,196,225,256,289,324,364,400]
my_orignal_list=my_list.pop(9)
print(my_orignal_list)"""

#find the output of code

"""x=[1,2,3]
y=x.pop(1)
print(x,y)"""

#can we store multiple data type in a list:=YES

"""list=["Ritik",21,32.2,True,[223],(5,4)]
for data_type in list:
    print(type(data_type))"""