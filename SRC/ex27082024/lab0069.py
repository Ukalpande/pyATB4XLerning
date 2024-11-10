#functions scope

global_b = 12 # almost  work like a globle veriable

def my_function():
    a = 11 # local variable, within the function
    print(a)
    print(global_b)

def f1():
    print(global_b)

my_function()
print(global_b)
f1()