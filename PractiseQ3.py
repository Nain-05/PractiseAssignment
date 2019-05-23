#3.	Write a Python function to check whether a number is completely divisible by another number.
#  Accept two integer values form the user

def myfunction(a,b):
    if a%b == 0:
        print('Number is Completely Divisible by another Number')
    else:
        print('Number is not completely Divisible by another Number')
    return
x=int(input('Enter Two Numbers:'))
y=int(input('Enter Another Number: '))
myfunction(x,y)
