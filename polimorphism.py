#polimorphism:

"""print(10+15)
print(type(10+15))

print("ritik"+"upadhyay!")
print(type("apna"))

print([1,2,3,4]+[2,3,4,5])
print(type([12334]))"""



# There are in polimorphism for using your personal opretaion creating we use dunder function:which is as:
# __add__ for = "+"
#__sub__ for = "-"
#__mul__ for = "*"
#__divtrue____ for ="/"
#__mode___ for "%"
  

#__add__
"""class complex:
    def __init__(self,real,imeg):
        self.real_no=real
        self.imeg_no=imeg

    def show_number(self):
        print(self.real_no ,"i +",self.imeg_no ,"j")

    
    def __add__(num1,num2):
        newrReal=num1.real_no + num2.real_no
        newIMeg=num1.imeg_no +num2.imeg_no
        return complex(newrReal,newIMeg)


num1=complex(2,4)
num1.show_number()

num2=complex(5,7)
num2.show_number()

num3=num1+num2
num3.show_number()"""


"""
class complex:
    def __init__(self,real,imeg):
        self.real_no=real
        self.imeg_no=imeg

    def show_number(self):
        print(self.real_no ,"i +",self.imeg_no ,"j")

    
    def __sub__(num1,num2):
        newrReal=num1.real_no - num2.real_no
        newIMeg=num1.imeg_no - num2.imeg_no
        return complex(newrReal,newIMeg)


num1=complex(2,4)
num1.show_number()

num2=complex(5,7)
num2.show_number()

num3=num1-num2
num3.show_number()"""




"""class complex:
    def __init__(self,real,imeg):
        self.real_no=real
        self.imeg_no=imeg

    def show_number(self):
        print(self.real_no ,"i +",self.imeg_no ,"j")

    
    def __mul__(num1,num2):
        newrReal=num1.real_no * num2.real_no
        newIMeg=num1.imeg_no * num2.imeg_no
        return complex(newrReal,newIMeg)


num1=complex(2,4)
num1.show_number()

num2=complex(5,7)
num2.show_number()

num3=num1*num2
num3.show_number()"""



"""class complex:
    def __init__(self,real,imeg):
        self.real_no=real
        self.imeg_no=imeg

    def show_number(self):
        print(self.real_no ,"i +",self.imeg_no ,"j")

    
    def __truediv__(num1,num2):
        newrReal=num1.real_no / num2.real_no
        newIMeg=num1.imeg_no /num2.imeg_no
        return complex(newrReal,newIMeg)


num1=complex(2,4)
num1.show_number()

num2=complex(5,7)
num2.show_number()

num3=num1/num2
num3.show_number()"""


"""class complex:
    def __init__(self,real,imeg):
        self.real_no=real
        self.imeg_no=imeg

    def show_number(self):
        print(self.real_no ,"i +",self.imeg_no ,"j")

    
    def __mod__(num1,num2):
        newrReal=num1.real_no % num2.real_no
        newIMeg=num1.imeg_no %num2.imeg_no
        return complex(newrReal,newIMeg)


num1=complex(2,4)
num1.show_number()

num2=complex(5,7)
num2.show_number()

num3=num1%num2
num3.show_number()"""


class complex:

    def __init__(self,real_num,imeg_num):

        self.real_num=real_num
        self.imeg_num=imeg_num
    
    def show_number(self):
        print(self.real_num ,"i +", self.imeg_num ,"j")

    def __add__(self,num2):
        real_number=self.real_num + num2.real_num
        imeg_number=self.imeg_num+num2.imeg_num
        return complex(real_number,imeg_number)
    
object=complex(2,3)
object2=complex(5,4)
object.show_number()
object2.show_number()

num3=object+object2
num3.show_number()