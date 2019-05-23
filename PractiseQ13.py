#13.	Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

Integer1= int(input('Enter two Integer:\n'))
Integer2= int(input())
if (Integer1 + Integer2) == 5 or (Integer1 - Integer2) == 5 or Integer1 == Integer2:
    Integer_flag = True
    print(Integer_flag)
else:
    Integer_flag = False
    print(Integer_flag)