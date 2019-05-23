#15.	Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

Amount = int(input("Enter Amount: "))
Interest = float(input("Enter Interest Rate: "))*0.01
Years = int(input("Enter No of Years: "))
Future_Value = round(Amount*((1+Interest)**Years),2)
print("Future Value: ",Future_Value)