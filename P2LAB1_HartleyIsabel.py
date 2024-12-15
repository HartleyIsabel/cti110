'''
Isabel Hartley
06 Oct 2024
P2LAB1
Using radius for the program to calculate the diameter, circumference, and area of a circle.
'''
import math
radius= float(input("What is the radius of the circle?"))
diameter= 2 *radius
circumference=  2 *math.pi*radius
area= math.pi * radius ** 2

print("The diamerter of the circle is",round(diameter,1))
print("The circumference of the circle is",round(circumference, 2))
print("The area of the circle is",round(area,3))

