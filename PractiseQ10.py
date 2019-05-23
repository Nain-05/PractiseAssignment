#10.	Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

Number=int(input('Enter Any Number: '))
if Number % 2 == 0:
    print('\nThe Number that You Entered is Even')
else:
    print('\nThe Number that You Entered is Odd')