#22.	Write a Python program to calculate body mass index. 

Height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
print("Your Body Mass index is: ", round(weight / (Height * Height), 2))
