"""
method overriding - same name in the parent and child

child always override the parent functions

super means call my parent function

"""

class Father:
    a=10
    def home(self):
        print("1bhk")

class Son(Father):
    def home(self):
        super().home() #-->(caling the parent class behavior by using super keyword ) calling super class function
        print(super().a) # also access parent class atributes by using super class
        print("NO House")
#self -- me
#super -- parent, father , super class
# super can be use within the class

ujwal = Son()
ujwal.home()