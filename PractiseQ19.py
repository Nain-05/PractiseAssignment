#19.	Write a Python program to convert the distance (in feet) to inches, yards, and miles. 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile

Distance = float(input('Please Input the Distance in feet: '))
Inches = float(Distance * 12)
Yard = float(Distance / 3)
Mile = float(Distance / 5280)
print("Distance in Inches: %.2f"%Inches)
print("Distance in Yard: %.2f"%Yard)
print("Distance in Mile: %.2f"%Mile)
