"""

> Static method
> Variables

1> Static Method
>> static method is a method that belongs to a class rather than an instance of the class.
>> static method can be called directly without the object.
>> static not belongs to object its belongs to class
>> static besicaly mens its belongs to directly class



TO access static methods it should be ---> Class NamemethodName
To access non static methods ---> (Object creation should be )-->> ref_variable /object.methodName
"""

class MathOperations:

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b
    @staticmethod
    def sub(a, b):
        return a - b

# NON STATIC METHOD --> NEED TO CREATE OBJECT
object_ref = MathOperations()
output = object_ref.div(10, 20)
output2 = object_ref.mul(2, 4)
print(output)
print(output2)

# STATIC METHODS CAN BE CALLED DIRECTLY WITHOUT OBJECT CREATION
print(MathOperations.sum(44, 2))
print(MathOperations.sub(50, 6))
