# date and times

import datetime
from traceback import print_tb

date = datetime.date(2025, 1, 2)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(12, 13, 25)
print(time)

now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d/%m/%Y")
print(now)

target_datetime = datetime.datetime(2022, 1, 2, 12, 13, 20)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print(f'Target date has passed')
else:
    print(f'Target date has not passed')

print("----------------------------------------------------------------------------")
print(f'Days : {today.day}')
print(f'month : {today.month}')
print(f'year : {today.year}')
#---------------🎯 Challenge---------------
#---------------- Calculate the days between two dates---------------

#diff = abs((current_datetime - target_datetime).days))
diff = (current_datetime - target_datetime).days
print(diff)
