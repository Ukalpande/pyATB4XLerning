"""
write a program to calculate the
area of the circle given its radius using the formula
area=n*r^2  (take pie as 3.14)

logic building furmula
out of the input and output
 stape1 - figure out the input amd out put
 input --> r data type --> float
 pi -> 3.14 or math.pi
 power -> pow or **-> any

 output --> float area, print area

stap 2. rogh logic = area = 3.14  + pow(r,2)

stape 3. write the logic


"""
import math

radius = float(input("Enter the radius of thr circle "))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 2)
print ("area of thr circle is,", area)
#using formating -->
print (f"area of thr circle is, {area:2f}")


# * -> multiplication
# ** -> power

