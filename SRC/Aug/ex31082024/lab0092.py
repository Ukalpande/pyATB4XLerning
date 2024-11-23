class person:

#Attribute
 id = None
name = None
age = None
email = None
height = None
gender = None
phone_no = None
address = None


# Behaviour


def talk(self):  # No return type no argument ) #self - this self will be first argument in every behaviour
    print(" i can talk")


def sleep(self, name):  # arg with no return type
    print(" i am a method!!")
    print("sleep", name)


def sleep2(self, name):  # arg with return type
    print("i am methid!!")
    return None


def walk(self):
    print("i am walking")


def walk_return(self):  # no arg return
    return "i am walking"

    # create an object of the class
    # objectref = classname() --> object

tushar = person()
tushar.name = "tushar"
print(tushar.name)

lakshmi = person()
lakshmi.name = "lakshmi"
print(lakshmi.name)


