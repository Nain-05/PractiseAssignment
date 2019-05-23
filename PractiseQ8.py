#8.	Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

Given_String = input('Enter your desire String: ')
New_String = Given_String
Add_String = 'Is' or 'is'
if Given_String[:2] == Add_String:
    print('String is Unchanged')
else:
    New_String = Add_String +" "+ Given_String
    print('New String: ', New_String)

