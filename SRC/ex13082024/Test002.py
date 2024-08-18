"""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""

num1 = int(input("Enter the num1 "))
num2 = int(input("Enter the num2 "))
max =max(num1, num2)
print(max)

pow = pow(num1, num2)
print(pow)

sum = (num1+num2)
print(sum)

mul = (num1*num2)
print(mul)

sub = ( num1-num2)
print(sub)

div = (num1/num2)
print(div)