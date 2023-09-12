# Exercise 1

# import datetime

# upcoming_holiday = "RoshHaShana"

# date_time_string = "2023-09-16"


# def current_date ():
#     curent_date = datetime.datetime.today()
#     return curent_date

# def time_to_holiday():
#     holiday_date = datetime.datetime.strptime(date_time_string, '%Y-%m-%d')
#     time_to_holiday = holiday_date - current_date()
#     return time_to_holiday

# print(time_to_holiday())



# Exercise 2

# orbital_periods = {
#         'Earth': 31557600,
#         'Mercury': 31557600 * 0.2408467,
#         'Venus': 31557600 * 0.61519726,
#         'Mars': 31557600 * 1.8808158,
#         'Jupiter': 31557600 * 11.862615,
#         'Saturn': 31557600 * 29.447498,
#         'Uranus': 31557600 * 84.016846,
#         'Neptun': 31557600 * 164.79132
#     }

# def my_age(planet, seconds):
#     for key in orbital_periods:
#         if planet == key:
#             planet_age = seconds/orbital_periods[key]
#             print(f"On the {key} your age is {round(planet_age, 2)}")

# my_age("Earth", 1000000000)
# my_age("Mercury", 1000000000)
# my_age("Venus", 1000000000)
# my_age("Mars", 1000000000)
# my_age("Jupiter", 1000000000)
# my_age("Saturn", 1000000000)
# my_age("Uranus", 1000000000)
# my_age("Neptun", 1000000000)

# Exercise 3

# import re

# def return_numbers(txt):
#     x = re.findall("[0-9]", txt)
#     print ("".join(x))

# return_numbers('k5k3q2g5z6x9bn') 

# Exercise 4

# import re

# user_input = input("Type your name:\n")

# def validate_name(user):
#     if re.match("^[A-Za-z]+ [A-Za-z]+$", user):
#         formatted_name = ' '.join([part.capitalize() for part in user.split()])
#         return formatted_name 
#     else: 
#         return None
    
# formatted_name = validate_name(user_input)
# if formatted_name: 
#     print(f"Valid name: {formatted_name}") 
# else: 
#     print("Invalid name")

# Exercice 5

import string
import random
import re

# while True:
#     user_input = int(input("Type your password lenth(from 6 to 30 characters):"))
#     if 6 <= user_input <= 30:
#         break
#     else:
#         print("Wrong number")

def generate_password(user_input):
    password = []
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(user_input):
        password.append(random.choice(characters))
    return "".join(password)

def validate_password(password):
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+{}|<>?]", password):
        return False
    return True

index = 0
while index != 1000:
    while True:
        password = generate_password(random.randint(6,30))
        if validate_password(password) == True:
            print(f"Your new password is: {password}\nKeep the password in a safe place!")
            break
        print("Wrong")
    index += 1