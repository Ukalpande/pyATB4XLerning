#understanding decoretors in python

#decoretor in python are a way to modify the beavior of a function or class without changing its scorce code
# two part in decoretor
# wrapper and call

#advantage

"""
def my_decoretor(func):

    def wrapper():
        print("1 something happening befour function ")
        print("2 helmate, spect, glabs")
        func()
        print("3 something is happening after the function" )
        print("4 safely driving")
    return wrapper()


# defination

@my_decoretor
def drive_bike():
    print("i am driving ")
#@my_decoretor
#def driving_scuty():
#    print("my scuty")

#call to the function
#drive_bike()
"""


#REAL EXAMPLE

def testcode (func): #FUNC IS THE COSTOME FUNCTION WHERE YOU WANT EXTRA FUNCTIONALITY

    def wrapper(): # WHAT YOU WANT YOU CAN NAME YOUA AS ANYTHING
        print(" before the testing code  ")
        print("code not tested unsafe code ")
        func()
        print("after the testing code " )
        print("tested no error,  code is safe ")
    return wrapper()


# defination

@testcode
def testing_c():
    print("ill testing code ")
