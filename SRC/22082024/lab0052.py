# match Statement
"""
match is switch statement in java
match the out put and execute

syntax :-
match variable:
     case pattern1:
     #code block
     case pattern2:
     code block

"""

#write a program to ask user which brouser he want to use to run autometion

browser_name = input("Enter the name of the browser\n")
match browser_name:
    case "firfox":
        print("Excute the firfox code")
    case "crome":
        print("Excute the crome code")
    case "edge":
        print("Excute the edge code")
    case "safari":
        print("Excute the safari code")