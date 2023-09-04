date = input("Type your birtdate (DD/MM/YYYY):\n")
date = date.split("/")
year = date[-1]
current_year = 2023
age = current_year - int(year)
candles = age % 10

candles = "i"*candles
print("    __"+candles+"__    ")