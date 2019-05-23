#18.	Write a Python program to calculate the hypotenuse of a right angled triangle

from math import sqrt
side_a = float(input('Enter the lengths of Triangle sides\n a: '))
side_b = float(input(' b: '))
C = float((side_a ** 2) + (side_b ** 2))
Hypotaneous = sqrt(C)
print("Hypotaneous of a Right Angled Triangle: %.1f"%Hypotaneous)