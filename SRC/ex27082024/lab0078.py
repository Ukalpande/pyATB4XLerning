

"""
lambda function
1, lambda function is an anonymous function
that return same from the data-

list
tuple
map and filters
set,dict
opps concept
"""

def triple_me(num):
    return num**3

o=triple_me(10)
print(o)

#lambda for the same expretion in one line

o= lambda num: num**3
print(o(10))


#ex2

def add_10(n):
    return n+10

#with lambda

o= lambda n: n+10
print(o(100))

#ex3

def mul(a,b):
    return a*b

#with lambda mul

oo = lambda a,b:a*b
print(oo(a=4,b=6))