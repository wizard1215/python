"""f=open("first.txt" ,"r")
data=f.read()
print(data)
print(type(data))
f.close()"""


# if we want to read only some specific data from file then we use the sach as slicing as :f=open("first.txt" ,"r")
"""f=open("first.txt" ,"r")
data=f.read(6)
print(data)
print(type(data))
f.close()"""


"""if we want to read data from file line by line then we use the radline function
like as """ 

"""
f=open("first.txt","r")

lin1=f.readline()
print(lin1)

line2=f.readline()
print(line2)"""

# we read first all data then the space is occured in output last:as
"""f=open("first.txt","r")
data=(f.read())
print(data)


lin1=f.readline()
print(lin1)

line2=f.readline()
print(line2)
f.close()"""