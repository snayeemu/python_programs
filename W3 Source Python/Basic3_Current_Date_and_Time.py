import datetime

time_and_date = datetime.datetime.now()
year = time_and_date.strftime("%Y")
month = time_and_date.strftime("%m")
date = time_and_date.strftime("%d")
todays_date = year + "-" + month + "-" + date

hour = time_and_date.strftime("%H")
minute = time_and_date.strftime("%M")
second = time_and_date.strftime("%S")
time = hour + ":" + minute + ":" + second

print(f"Todays date is: {todays_date}")
print(f"Time is: {time}")