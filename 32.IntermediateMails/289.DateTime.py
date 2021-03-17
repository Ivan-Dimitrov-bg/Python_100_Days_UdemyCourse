import datetime as dt
# GET
now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
print(month)

day_of_week = now.weekday()
print(day_of_week)  # start from 0

#SET
date_of_birth = dt.datetime(year=1985, month=8, day=22, hour=12)
print(date_of_birth)

