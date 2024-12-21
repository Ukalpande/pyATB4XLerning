
"""
#polymorphism ex..>
#method overriding
#says that child or subclass can have a same name method as the parent or super class
"""


class Shape:
    def area(self):
        print("the area of the shape ")


class Rectangle(Shape): # it si a single inheritance
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length*self.width
class Circle(Shape):  # it is herarical inheritance

    def __init__(self, redius):
        self.redius = redius


    def area(self):
        return 3.14*self.redius*self.redius

shape1 = Rectangle(3, 4)
print(shape1.area())


shape2 = Circle(10)
print(shape2.area())

 