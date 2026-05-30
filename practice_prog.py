# 1 Create a file which name is practice.txt and cotaining the data:

"""f=open("practice.txt","a")
f.write("HII everyone.\n we are learning file i\o.\n from JAVA.\n using apna college channel.")
f.write("\n i like programming in JAVA.")"""



# WAP where the replace the all occurence of JAVA change into python:
"""with open("practice.txt","r") as f:
    data=f.read()
    
new_data= data.replace("JAVA","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)"""

# search for if the word learning is exist in the this file:
"""with open("practice.txt","r") as f:
    data=f.read()
    print(data)
     
word="learning"
if data.find(word)!=-1:
    print("found")
else:
    print("not found")"""

# WAF and cheack that which line in file the word learning is exist if not exist then print -1:

def check_line_num():
    word="learning"
    line_num=1
    with open("practice.txt","r") as f:
        while(True):
            data=True
            data=f.readline()
            if data=="":
                break
            elif word in data:
                print("word is found at line",line_num)
            line_num+=1
        return -1
check_line_num()















    