from datetime import date
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
difference = last_date - first_date
print("days between {} and {} is {}".format(first_date, last_date, difference.days))