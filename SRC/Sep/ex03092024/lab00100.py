# class variable
# instance variable
# name = "ujwal"  # if you asain  the variable in the class it becomes hard coded value, comman across all variable

class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name

amit = Person("amit")
pramod = Person("pramod")
print(amit.name)
print(pramod.name)
print("who is walking with the object pramod-->", pramod.walk())