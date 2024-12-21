"""
try:
    try this code, if error

    except :
    except me if try has some error


"""


import math

try:
    math.exp(1000) #OverflowError: math range error
except Exception as e:
    print(e)
    print(" please try to use lower number ")