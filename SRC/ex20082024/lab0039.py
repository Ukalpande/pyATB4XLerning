# max between 3 number

# Logic building formula

# user input num1 , num2, num3 int type
# o/p is int or string with max num

# Logic ..? if else - 1 condition
# for multiple condition --> if elif else

# syntax -->

# if condition 1:
# print ("do 1")
# elif condition 2:
# print ("do 2")
# else:
# print("do 3")

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

# num 1 > num2 and num1 > num3 ->num1
# num 2 > num1 and num2 > num3 ->num2


if num1 > num2 and num1 > num3:
    print("max is", num1)

elif num2 > num1 and num2 > num3:

    print("max is ", num2)

else:
    print(" max is", num3)
