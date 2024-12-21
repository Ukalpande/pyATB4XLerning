
"""
#Encapsulation
bind the data variables with the methods
data members -/ class variables
methods  def function within the class
wrapping or binding the data variables with the methods - encapsulation



"""

class Car:
    name = None
    password = 123
    def __init__(self):
        self.password = "ujwal"
        # self.password = "ujwal"
    def change_password(self):
        self.password = "ujwal"
        print(self.password)


object_ref = Car()
print(object_ref.password)
object_ref.change_password()