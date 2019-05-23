#21.	Write a Python program to convert seconds to day, hour, minutes and seconds.

Time = int(input('\nEnter Time in Seconds:\n'))
Days = int(Time / (24*3600))
Time = Time % (24*3600)
Hours = int(Time / 3600)
Time %= 3600
Minutes = int(Time / 60)
Time %=  60
Seconds = int(Time)

print('\n\t\td:h:m:s')
print("\n\t\t" + str(Days) + ":" + str(Hours) + ":" + str(Minutes) + ":" + str(Seconds))