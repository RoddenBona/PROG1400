from datetime import datetime, timedelta

decimal_time = 1711629855
decimal_time_offset = -10800 #halifax
epoch = datetime(1970, 1, 1) #unix epoch
timestamp = epoch + timedelta(seconds = decimal_time)
print(f"{timestamp}")
current_time = timestamp + timedelta(seconds=decimal_time_offset)
print(f"{current_time.day}")
print(f"{current_time.month}")
print(f"{current_time.year}")

weekday = current_time.strftime("%A")
print(weekday)

print(f"{current_time.strftime("%Y %m-%d-%y %H:%M:%S")}")
print(f"{current_time.strftime("%Y %B-%d, %Y %H:%M")}")
print(f"{current_time.strftime("%a %b-%d, %Y %H:%M %p")}")