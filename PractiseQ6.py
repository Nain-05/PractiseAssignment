from math import pi
radius=float(input('Enter Radius of Sphere: '))
a=float(4/3)
R=float(radius*radius*radius)
VolumeSphere = float(a*(pi*R))
print("Volume Of Sphere: %.3f"%VolumeSphere)