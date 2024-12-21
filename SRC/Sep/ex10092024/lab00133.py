
#try and except consept



print("start of the program ")
try:
    a = int(input("Enter rhe num1")) #ValueError: invalid literal for int() with base 10: ' ujwal'
    b = int(input("Enter rhe num2"))
    c=a/b #ZeroDivisionError: division by zero- lab00132.py, line 3

    print(("Result Div is ", c))
except Exception as e:
    print(e)
    print("Please check input, its should  be a string or zero")

    print(" end of the program ")

