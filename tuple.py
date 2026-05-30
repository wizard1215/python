# tuple is a immutable data type in python it store multiple value in a variable and it store the data into paranthesis():

"""my_tuple=(1,2,3,4,5,6,7,8,9,10)
my_tuple(0)==5
print(my_tuple)#error"""

#slicing in tuple:

"""marks=(90,80,50,60,70,40,33,96,95,100,21,22,35,45,42)
marks1=marks[0:9]
print(marks1)"""
 
# negative slicing in tuple:
"""marks=(90,80,50,60,70,40,33,96,95,100,21,22,35,45,42)
marks1=marks[-5:-1]
print(marks1)"""
 
#len of tuple:
"""my_tuple=(90,80,50,60,70,40,33,96,95,100,21,22,35,45,42)
print(len(my_tuple))"""

#concatination:
"""tuple1=(90,80,50,60,70,40,33,96,95,100,21,22,35,45,42)
tuple2=(2,4,9,16,25,36,49,64,81,100)
final_tuple=tuple1+tuple2
print(final_tuple)
"""
#there are only two methods of tuple:
#1.index()
"""tuple1=(90,80,50,60,70,40,33,96,95,100,21,22,35,45,42,100)
tuple2=tuple1.index(100)
print(tuple2)"""

#2.count()
"""tuple1=(90,80,50,60,70,40,33,96,95,100,21,22,35,45,42,100)
tuple2=tuple1.count(100)
print(tuple2)"""


# to count the number of students with the "A" grade in the following tuple:
"""Tuple=("C","D","A","A","B","B","D","E","A","A")
tuple=Tuple.count("A")
print(tuple)"""

#store the given value in a list and sort them from "A",to "D":
#Tuple=("C","D","A","A","B","B","A")
list1=["C","D","A","A","B","B","A"]
#list2=list1.sort()
#print(list1) 

#can we store the diffrente data type value ina tuple:YESS

"""Tuple=("Ritik",21,32.2,True,[223])
for data_type in Tuple:
    print(type(data_type))"""




