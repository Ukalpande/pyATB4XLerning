# Gread Calculator

# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g. A,B,C,D OR F)
# base on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# C: 0-59

marks = int(input("ENTER THE MARKS"))

if marks >= 90  and marks <= 100:
    print("your Gread is A")
elif marks >= 80 and marks <= 89:
    print("your Gread is B")
elif marks >= 70 and marks <= 79:
    print("your Gread is C")
elif marks >= 60 and marks <= 69:
    print("your Gread is D")
elif marks >= 0 and marks <= 59:
    print("your are fail ")

else:
    print("error unable to display result")