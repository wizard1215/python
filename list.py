# list is a mutable sequence type in Python.and here is slicing is posssble

"""name=["Ritik","ravi","sonna"]
name[0]="ravi"
print(name)  """

# Output: ['ravi', 'ravi', 'sonna']

"""list1=[1,2,3,4,5]
list1[2]="5"
print(list1)"""

#slicing work as same as in string

"""marks=[90,80,50,60,70,40,33,96,95,100,21,22,35,45,42]

marks1=marks[0:11]
print(marks1)"""

#negative slicing are offered:

"""marks=[90,80,50,60,70,40,33,96,95,100,21,22,35,45,42]
marks1=marks[-10:-1]
print(marks1)"""


#11.copy()
"""marks=[90,80,50,60,70,40,33,96,95,100,21,22,35,45,42]
marks_1=marks.copy()
print(marks)"""


#Wap to ask the user thier three favorite movie name and  add in a  list:
movies=[]
"""
movie1=input("enter the first favorite movie name:")
movie2=input("enter the second favorite movie name:")
movie3=input("enter the third favorite movie name:")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)"""

#wap to check a list contain a palindrome elements in a list:
"""list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")"""

"""list1=[90,80,50,60,70,40,33,96,95,100,21,22,35,45,42]
print(min(list1))
print(max(list1))"""


#remove duplicate elements from a list:
"""list1=[90,80,50,60,70,80,80,40,33,80,96,95,100,21,22,35,45,42,100]
list1=list(set(list1))
print(list1)"""

#wap to check that a list is palindrome or not:
"""list=input("enter the any list:")
list1=list.split()
if list1==list1[::-1]:
    print("list is palindrome")
else:
    print("not palindrome")"""


# find the output of this code :
"""words=["apple","banana","cherry","date"]
lengths=[]
for word in words:
    lengths.append(len(word))
print(lengths)"""


# find the output of this code:
"""a=[1,2,3]
b=a
a=a+[4]
print(b)"""

