#24.	Write a python program to sum of the first n positive integers

N = int(input('Enter positive Integer: '))
sum = 0
for i in range(1,N+1):
    sum = sum + i
print("Sum of first n positive Integer: ", sum)

