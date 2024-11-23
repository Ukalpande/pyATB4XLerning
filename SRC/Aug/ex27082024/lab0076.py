import functools


#@staticmethod
#@classmethod
#@property
#@functools.wraps
#these will be use in oops consept
#Chaining decoretor

def decoretor_1(func):
    def wrapper():
        print("decoretor_1")
        func()

    return wrapper

def decoretor_2(func):
    def wrapper():
        print("decoretor_2")
        func()
    return wrapper

@decoretor_1   #two deocretor decoreror 1 and 2
@decoretor_2
def say_hello():
    print("hELLO")

say_hello()

"""
primery use of decoretor 

1, before
2, after
3, logging- add log stor autometion 


"""
