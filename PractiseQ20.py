#20.	Write a Python program to convert all units of time into seconds.

Days = int(input('Enter Days: ')) * (24*3600)
Hours = int(input('Enter Hours: ')) * 3600
Minutes = int(input('Enter Minutes: ')) * 60
Seconds = int(input('Enter Seconds: '))
Time_in_seconds = int(Days + Hours + Minutes + Seconds)
print('Units of Time in Seconds:',Time_in_seconds) 