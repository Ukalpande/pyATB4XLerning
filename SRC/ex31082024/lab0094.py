#constractor
#special function in class __init__()
# it will be autometically called when you reate an object
#from SRC.ex31082024.lab0093 import Dog
#constructor is automaticlly call when you create an object

#two types of constructor
# 1, defult constructor
# 2, parameterised construtctor
# costructor dosent have any return type
# name of the costructor is __init__
# self mins current object 


class Dog:
    name = None

    def __init__(self, name):
        print("called object is created")
        self.name = name

        #this function behaive diffrently __init__
    def sleep(self):
        print("sleeping")

dog1 = Dog("chow")
print(dog1.name)


dog2 = Dog("mow")
print(dog2.name)

#with multipul argument -->


class Dogg:
    name = None
    age = None

    def __init__(self, name,age):
        print("called object is created")
        self.name = name
        self.age = age
        #this function behaive diffrently __init__
    def sleep(self):
        print("sleeping")
        print("who is sleeping-->"+ self.name)


dog4 = Dogg("chow", 20)
print(dog4.name)
dog4.sleep()


dog5 = Dogg("mow", 14)
print(dog5.name)
dog5.sleep()
