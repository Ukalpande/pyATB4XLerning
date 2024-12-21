#try , except and finally

try:
    num1 = int(input("enter the num 1\n"))
    num2 = int(input("enter the num 2\n"))
    result = num1/num2
except Exception as ve:
    print("value error, you have entered the string instead we want int")
except ZeroDivisionError as zde:
    print("Zero div error, dont use the num2 as 0")
else:
    print(f"Result is {result}")
finally:
    print("this code is always executed ")