# use of del keyword the del keyword is use to remove the key or attribute of any object themeselves :

"""class students:
    def __init__(self,name):
        self.name=name

object=students("Ritik_upadhayay!")
del object.name
print(object.name)"""


"""class person:
    name="Ritik"
    colour="black"
    hands="two"

Person=person()
del Person.name 
del Person.colour
del Person.hands

print(Person.name)
print(Person.colour)
print(Person.hands)"""
        
#private attribute!
# in the below example there are two key in a class where 
#the account_no=private attribute(private key) and 
#the acount_pass is a public key which we can access directley:

"""class account:
    def __init__(self,account_no,account_pass):
        self.account=account_no
        self.__account=account_pass


    def get(self):
        return self.__account
    
    def set(self,account_pass):
        self.__account=account_pass

        
Account=account(50526616442,12345)
print(Account.account)
print(Account.get())"""

