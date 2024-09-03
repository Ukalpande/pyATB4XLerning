# Task #8
"""Triangle Classifier:
Write a program that classifies a triangle
based on its side lengths.
Given three input values representing the lengths
 of the sides,
determine if the triangle is equilateral
 (all sides are equal),
isosceles (exactly two sides are equal),
 or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""

side1 = int(input("Enter the side1 of the triangle "))
side2 = int(input("Enter the side2 of the triangle "))
side3 = int(input("Enter the side3 of the triangle "))

if side1 == side2 and side1 == side3:
 print(" Equilateral - all side are equal")
elif side1 == side2 and side1 != side3:
    print(" isosceles -two of them are equal")
elif side1 == side2 and side1 != side3:
    print("The Triangle is isosceles")
elif side1 == side3 and side1 != side2:
    print("The Triangle is isosceles")
elif side2 == side3 and side2 != side1:
    print("The Triangle is isosceles")
else:
    print(" Scalene -no side are equal")