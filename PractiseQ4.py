#4.	Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)

#N=int(input('Enter any Number: '))
#Value = N + (N*N) + (N*N*N)
#print("Computed Value: ", Value)

#BY LOOP
for i in range(1,4):
    if i==1:
        A=N
    if i==2:
        B=N*N
    if i==3:
        C=N*N*N
Value=A+B+C
print("Computed Value: ", Value)  