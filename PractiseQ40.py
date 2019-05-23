#40.	Write a Python program that accepts a string and calculate the number of digits and letters Sample Data : Python 3.2, Expected Output : Letters 6, Digits 2


String = input("Enter any String: ")
Letters=0
Digits=0
for i in String:
    if i.isalpha():
        Letters = Letters+1
    elif i.isdigit():
        Digits = Digits+1
    else:
        pass
print("Number of Letters: ",Letters)
print("Number of Digits: ",Digits)
