# firstly we open it in write mode  hence occured the change or 
# overwrite into the files :

"""f=open("second.txt","w")
data=f.write("i am doiong b.tch from electrical :")
print(data)
f.close()"""


# now we use the the append method it is add the end of file:
f=open("second.txt","a")
data=f.write("\n so my name is ritik")
print(data)
f.close()