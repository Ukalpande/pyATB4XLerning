"""
user define function
1, they can return something
2, they can't return
3, they have parameters
4, they don't parameter and arguments


"""

#1,no return type and no agrument/ parameter
def greet():
    print("hello world")


result = greet()
print(result)
#2, no return type with argument
def greet_by_name(name):
    print("hello", name)

greet_by_name("ujwal")

#3, no return type with defult argument

def say_hello_defult_arg(name="ujwal"):
    print("hello", name.upper())

say_hello_defult_arg("prajakta")
say_hello_defult_arg()
say_hello_defult_arg(name="up") #positional argument


#multipul argument

def multiple_arg(name1="prajakta", name2="ujwal", name3="kalpande"):
    print("full name",name1,name2,name3)
multiple_arg()

#argument + return type

def sum_of_two_number(num1,num2):
    return num1 + num2
result = sum_of_two_number(num1=12, num2=21)
print(result)
result= sum_of_two_number(23,20)
print(result)

#with defult valnue
