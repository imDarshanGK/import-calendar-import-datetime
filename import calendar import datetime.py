import calendar
import datetime
print(calendar.calendar(2023))
print(calendar.month(2023,4))
print(calendar.isleap(2023))
print(calendar.weekday(2023,4,8))
print(datetime.date.today().weekday())
print(datetime.date.today().month)
print(calendar.day_name[datetime.date.today().weekday()])
print(calendar.month_name[datetime.date.today().month])
