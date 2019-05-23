
n = int(input('Enter no of rows: '))

for i in range(n):
    k = 1
    for j in range(0,i+1):
        print(k, end=" ")
        k = k+1
    print("\n")

for i in range(n,0,-1):
    k=1
    for j in range(i-1):
        print(k,end=" ")
        k=k+1
    print("\n")
