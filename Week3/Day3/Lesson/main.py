# Exercise 1

import datetime

today_date = datetime.date.today()
actual_datetime = datetime.datetime.now()
my_birthday = datetime.datetime(2024,5,1,4,30)
delta = my_birthday - actual_datetime

# print(f"Today is the {today_date.strftime('%d/%m')}")
print(f"My birthday will be in {delta}")