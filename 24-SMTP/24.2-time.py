import datetime as dt

actual_time = dt.datetime.now()
year = actual_time.year
month = actual_time.month
day = actual_time.day
day_of_week = actual_time.weekday()
date_of_birth = dt.datetime(2005, 4, 20)
print(date_of_birth)