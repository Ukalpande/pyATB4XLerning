"""

Abstraction --->>>

>>Hiding the details and showing the what is required

>>abstraction in a python is fundamental consept of object-oriented programming
>>focuses on hiding complex implementation details while exposing only the essential features of an object
>>ABC is the abstract class
>>it is the helper class that provide a standard wy to create an ABC using inheritance


To Create and abstract class in python you need to -:>>>
1>> import the "ABC" class and the abstractmethod decorator from the "abc" module.
2>> Define the clss that inherits from "ABC"
3>> Use the @abstractmethod decorator to define abstract methods.

"""


from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Ujwal(Father):
    def loan(self):
        print("paid the loan ")


ujwal = Ujwal("1 lk")
ujwal.loan()