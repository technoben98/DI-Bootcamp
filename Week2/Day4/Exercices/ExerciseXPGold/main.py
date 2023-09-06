# Exercise 1

# current_year = 2023
# current_month = 9
# current_day = 6
# gender = input("Type your gender(m/f): ")
# date_of_birth = input("Type your birthdate (YYYY/MM/DD):\n").split("/")
# year = 0
# month = 0
# # age = 0

# def get_age(year, month, day):
#     age = current_year - year
#     if month > current_month or (month == current_month and day > current_day):
#         age -= 1
#     return age

# def can_retire(gender, date_of_birth):
#     year = int(date_of_birth[0])
#     month = int(date_of_birth[1])
#     day = int(date_of_birth[2])
#     age = get_age(year, month, day)
#     if gender == 'm':
#         if age >= 67:
#             return True
#         else:
#             return False
#     else:
#         if age >= 62:
#             return True
#         else:
#             return False

# if can_retire(gender, date_of_birth) == True:
#     print("Nice, you can retire")
# else:
#     print("Sorry, you need to work now :(")

# Exercise 2

# def sum_of_x (x):
#     x = str(x)
#     xx = x + x
#     xxx = x + x + x
#     xxxx = x + x + x + x
#     summary = int(x) + int(xx) + int(xxx) + int(xxxx)
#     return summary
# print(sum_of_x(3))


# Exercise 3

import random

def trow_dice():
    return random.randint(1,6)

def throw_until_doubles():
    count = 0
    while True:
        dice1 = trow_dice()
        dice2 = trow_dice()
        count +=1
        if dice1 == dice2:
            return count
print(throw_until_doubles())

def main():
    total_count = 0
    how_much_doubles = 0
    while how_much_doubles <= 100:
        total_count += throw_until_doubles()
        how_much_doubles +=1
    print(f"For 100 doubles we throwed {total_count} times.")
    print(f"Average throws is: {total_count/100}")

main()