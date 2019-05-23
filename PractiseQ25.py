#25.	Write a Python program to calculate the sum of the digits in an integer

x=int(input("Enetr Digit: "))
x=str(x)
count=0
for i in range(len(x)):
    count=count+int(x[i])

print(count)