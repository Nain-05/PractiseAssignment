#39.	Write a Python program to create the multiplication table (from 1 to 10) of a number

Num = int(input("Enter any Number for which you want Multiplication Table: "))
for i in range(1,11):
    Table= Num * i
    print("         " + str(Num) + "  x  " + str(i) + "  =  " + str(Table))