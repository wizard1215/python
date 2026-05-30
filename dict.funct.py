"""
dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
print(dict)"""


#1.dict.keys()
"""dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
Dict=dict.keys()
print(Dict)"""

#2.dict.values:
"""dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
Dict=dict.values()
print(Dict)"""

#3.clear()
"""dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
Dict=dict.clear()
print(Dict)"""

#4 dict.item()"""
"""dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
Dict=dict.items()
print(Dict)"""


#5 dict.copy()
"""dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
Dict=dict.copy()
print(Dict)"""

#6.dict.pop()
"""dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
Dict=dict.pop("subject")
print(Dict)"""


#7.dict.get()

"""dict={
    "name":"ritik_upadhyay",
    "age":21,
    "subject":["math,physics","chemistry","java","python"],
    "marks":(21,44,63,78,89)
}
Dict=dict.get("subject")
print(Dict)"""

#8 dict.update()
"""dict1={ "name":"Ritik","age":21,}
dict2={"name":"Ravi","age":20}
dict=dict1.update(dict2)
print(dict1)"""


#wap to programme enter the marks of three subject from user and add in a dictonary and add them in dictonary one by one:
#use subject key and marks as value:

"""marks={}
a=int(input("enter the python marks:"))
marks.update({"python":a})
a=int(input("enter the java marks:"))
marks.update({"java":a})
a=int(input("enter the math marks:"))
marks.update({"math":a})
print(marks)"""


"""store a following word meaning in python dictonary:
table="a pieces of furniture","list of facts and figure"
cat="a small animals"""
"""dictonary={
    "cat":"a small animal",
    "table":["a pieces of furniture", "list of facts and figure"]
}
print(dictonary)"""

# you are giving a list of subject for students .assume one classroom is required for one subjects 
# how may classroom is needeed by all students:
"""subjects={"python","java","c++","python","javascript","java","javascript","java","c++","c"}  
print(subjects)
print(len(subjects))"""  