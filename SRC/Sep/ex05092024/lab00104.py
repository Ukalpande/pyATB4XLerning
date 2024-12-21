"""
Encapsulation



"""


class Myclass:
    #public variable (instance variable)
    public_var = "i am public"
    balance = "0"
    __private_var = "i am the private "
    #  starting from dubble underscore variable is the private variable
    __password = "1234"
    _protected_var = " i am protector "# starting from single underscore variable is protector

object = Myclass()
print(object.public_var) # public variable easly acessabe by creating object
print(object.balance)
print(object._protected_var) #protector is available in same pakage#

#print(object.__private_var) #you can not access private variable outside the class

