#16.	Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
from math import sqrt
from math import pow
x1 = 5
x2 = 4
y1 = 3
y2 = 6
Distance = round(sqrt(pow((x1-y1),2) + pow((x2-y2),2)))
print("Distance between the Points is: ",Distance)