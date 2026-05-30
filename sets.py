# How to create a empty set:
"""set1={1,2,3,4,5,5,5,23,3,4,10,11}
print(set1)"""

# Add 10 in set usning add method:

"""set={1,2,3,4,5,6,7,8,9}
adding=set.add(10)
print(set)"""


# Remove 3 from the set:

"""set={1,2,3,4,5,6,7,8,9,10}
adding=set.remove(3)
print(set)"""

# Cheack that 5 is exsit in set or not:

"""set={1,2,3,4,5,6,7,8,9,10}
print(5 in set)"""

# Create Two set find union both:
"""set1={1,2,3,4}
set2={3,4,5,6}
union_set=set1.union(set2)
print(union_set)"""

# Create Two set and find intersection  both:
"""set1={1,2,3,4}
set2={3,4,5,6}
intersection_set=set1.intersection(set2)
print(intersection_set)"""


# find the diffrence of two sets:
"""set1={1,2,3,4}
set2={3,4,5,6}
diff=set1.difference(set2)
print(diff)"""

# in a set try to add a list like [7,8] occured error or not:
"""set={1,2,3,4,5,6,7,8,9,10}
list=[7,8]
var=set.add(list)
print(var)"""


# convert the set into list:
"""set={1,2,3,4,5,6,7,8,9,10}
l=list(s)
print(type(l))"""


# create a set and add set "Ritik"

"""set={1,2,3,4}
adding=set.add("Ritik")
print(set)"""

# create a set and find its length:
"""set={1,2,3,4,5,6,7,8,9,10}
print(len(set))"""


# create a set and clear all value from the set:
"""set={1,2,3,4,5,6,7,8,9,10}
set.clear()
print(set)"""


# check any two seta are equal or not:
"""set1={1,2,3,4,5,6,7,8,9,10}
set2=set1
print(set1 is set2)
print(id(set1))
print(id(set2))"""


# create a set stote only even number from 0 to 10:

"""set1=set()
for i in range(0,11):
    if i %2 ==0:
        set1.add(i)
print(set1)"""
    
    



