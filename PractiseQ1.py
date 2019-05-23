#1.	Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi
radius=float(input("Enter the radius of the Circle: "))
Area_of_Circle= float(pi *(radius*radius))
print('Area of the Cirle: %.2f' %Area_of_Circle)
