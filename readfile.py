# Wap to open the three file 1.txt,2.xt,3.txt if any of three files are not present then .
# message without exiting the programme must be printed promoting the same: 

"""def readFile(filename):
  try:  
    with open(filename,"r") as f:
     print(f.read())
  except FileNotFoundError:
    print(f"the file {filename} is not exist in this folder....")


readFile("1.txt")
readFile("2.txt")
readFile("3.txt")"""


#wap to print the third ,fifth and seventh element from a list using enumrating function..

"""num=[2,3,4,5,6,7,9,10,12,3,14,20,78,98,100,20]
for index,number in enumerate(num):
    if index in (3,5,7):
     print(index,number)"""


#wap to print the user entered table with using the list comperhension: 
"""table=int(input("enter any  number..."))
table1=[table*i   for  i in   range(1,11)]
print(table1)"""



# wap to display a/b where a and b are the integer if b=0 display  infinite by handling the zerodivissionerror: 

'''while(True):
 try:
  a=int(input("enter the number..."))
  b=int(input("enter the number..."))
  c=a/b
  print(c)
 except Exception as e:
  print("infinite..")'''

# store the multiplication  tables genreated  in problems 3 in a file named Tables.txt.
while(True):
 table=int(input("enter the table number.."))
 tab1=[table*i for  i in range(1,11)]
 print(tab1)
 with open("table.txt","a") as f:
    f.write(str(tab1))
    f.write("\n")
