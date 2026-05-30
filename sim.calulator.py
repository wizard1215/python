# Simple Calculator Program:
print("1=addition:")
print("2=subtraction")
print("3=multiplication:")
print("4=divission:")

choice=int(input("enter any no.according to your  choice:"))

num1=int(input("enter the first number:"))

num2=int(input("enter the second number:"))

if(choice==1):
    print("the addition is :",num1+num2)

elif(choice==2):
    print("the subtraction is :", num1-num2)

elif(choice==3):
    print("the multiplication is :", num1*num2)

elif(choice==4):
    print("the division is :", num1/num2)

else:
    print("invalid input, please try again")