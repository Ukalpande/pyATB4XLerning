#Task #4
#- Write a Python program to calculate the area of a circle
# given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
import math

radius = float ( input( " Enter the radius of circul "))
print(radius)
print(math.pi)

area = math.pi * math.pow(radius, 2)
print (" area of the circul", area)



