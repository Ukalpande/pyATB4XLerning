#create a program to sum of three number from user inpts


num1 = int(input("enter the number 1"))
num2 = int(input("enter the number 2"))
num3 = int(input("enter the number 3"))


def sum_of_three_number(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_number(num1, num2, num3)
print(result)
result = sum_of_three_number(n1=num1, n2=num2, n3=num3)
print(result)
