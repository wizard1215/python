#string is immutable data type in python:
#we can create a string with three method:
string1="my name is Ritik"
string2="""my nameis Ritik"""
string3='''my name is Ritik'''


"""string1="my name is Ritik and \n my age is 21 years old"

string2="i am read python from apna college of b.tech"
print(string1)
print(string2)"""



# use of \t=tab space
"""string_a="hello\tworld"
print(string_a)"""

#when we add two string this is called concatination:
"""string1="my name is Ritik"
string2="i am 21 years old"

final_string=(string1 +" "+ string2)
print(final_string)"""


# length of string:

"""string1="i am read python from apna college channel"
string2="i studying in b.tech 4th years"
final_string=len(string1) +len(string2)
print(final_string)

string_a="Ritik"
string_b="upadhyay"
final_string=len(string_a) + len(string_b)
print(final_string)"""


# indexing in string:

"""name="Ritik_upadhyay"
name1=(name[3])
print(name1)#i

string1="Hii Ritik how are you:"
string2=(string1[4])
print(string2)#R"""



# positive slicing in python:
"""string3="hii Ritik welcome to you in visual studio code:"
string4=(string3[0:9])
print(string4)


string_a="Ritik is bad boy because he is not study in python:"
string_c=string_a[0:]
print(string_c)

string_a="Ritik is bad boy because he is not study in python:"
string_c=(string_a[:28])
print(string_c)"""

#nagative slicing in python:

"""string1="hello world:"
string2=(string1[-6:-1])
print(string2)

string_5="Ritik is cool boy:"
string_10=string_5[:-1]
print(string_10)"""



#functions of string 
#1. enswidth function
"""string1="hii Ritik how are you"
string2=(string1.endswith("ou"))
print(string2)

string2="HEY RAM!"
string_3=string2.endswith("r!")
print(string_3)"""

#2.capitalize function:
"""string1="hii ritik what are you doing now:"
string2=(string1.capitalize())
print(string2)
print(string1.capitalize())"""

#3.replace function:
"""string_A="hii do you now"
string_B=string_A.replace("hii","what")
print(string_B)
print(string_A)"""

#4.find Word function:

"""string1="hello anshika verma how are you:"
string2=string1.find("a")
print(string2)

string_A="hello ritik wahts are you doing now:"
string_B=string_A.find('r')
print(string_B)"""

#5.count finction:

"""string_A=" Ritik village name is shafipur:"
string_B=string_A.count("R")
print(string_B)"""


#6.upper function:
"""str_1="hii ritik where are you live now a days:"
str_2=str_1.upper()
print(str_2)


#7.lower function:
str1_5="HII RITIK WHERE ARE YOU LIVE NOW A DAYS:"
str_6=(str1_5.lower())
print(str_6)"""


#practice quesstion:
#WAP TO TAKE INPUT FROM USERAS A STRING AND PRINT THE LENGTH OF STRING:
"""str_A=input("enter a string:")
str_2=(len(str_A))
print(str_2)"""

#wap to find occurence of $ in a string which is given as :
"""str_A="hii am symbol of $ I am a American doller($) my value in america is 90 in indiane ruppees:"

str_2=str_A.count("$")

print(str_2)"""







