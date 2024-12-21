"""
Method overloading
Python does not support method overloading

in the traditional sense

"""
#method overloading not supported  in python

class MathUtils(object): # is a single Inheritance
#OBJECT IS BYDEFULT PRESENT IN THE CLASS

    #def add(self,a, b):
     #   return a + b
    def add(self,a,b,c=12, d=10):
        return a + b + c + d

math = MathUtils()
op1 =math.add(2,4)
print(op1)