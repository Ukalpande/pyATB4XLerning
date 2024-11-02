"""
def print_argument(*args):
    #*args = multiple argument with no limit,--> list
    #no return type in *args fiuction
    print(args[0])
print_argument("ujwal","rajesh","shubham")
print_argument("shubham", "gopal")
print_argument("gopal",10)
print_argument("gopal",10, False, True)
print_argument("gopal",10, False, True, "UJWAL")

#print_argument + minimum 1 argument is requrted
"""
import args


def print_argument(*args):
    #*args = multiple argument with no limit,--> list
    #no return type in *args fiuction
    for i in args:
        print(i)
print_argument("ujwal","rajesh","shubham")
print_argument("shubham", "gopal")
print_argument("gopal",10)
print_argument("gopal",10, False, True)
print_argument("gopal",10, False, True, "UJWAL")




