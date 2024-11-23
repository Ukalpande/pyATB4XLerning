class Person:
    # class variable
    # instance variable
    name = "ujwal"  # if you asain  the variable in the class it becomes hard coded value, comman across all variable


def __init__(self, name):
    self.name = name


def walk(self):
    print(self.name)


ujwal = Person()
pramod = Person()
print(ujwal.name)
print(pramod.name)
