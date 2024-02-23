import datetime as dt

date1 = dt.datetime(2023,12,25,0,0,0)
date2 = dt.datetime(2024,2,5,0,0,0)

date_diff = date2 - date1

print(date_diff.total_seconds())