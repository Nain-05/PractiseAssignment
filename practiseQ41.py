#41.	Write a Python program to construct the following pattern, using a nested for loop

n = int(input("Enter no of rows: "))
for i in range (0,n):
    for j in range(i+1):
        print("*", end=' ')
    print("\n")

for i in range (n, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\n")