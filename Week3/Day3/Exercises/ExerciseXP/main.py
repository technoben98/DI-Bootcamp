# 🌟 Exercise 1: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     #Your code starts HERE


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

#-------------------------------------------------------------------------------------------------------------

# ANSWER

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         if self.amount > 1:
#             return f"{self.amount} {self.currency}'s"
#         else:
#             return f"{self.amount} {self.currency}"
        
#     def __int__(self):
#         return self.amount

#     def __repr__(self) -> str:
#         if self.amount > 1:
#             return f"{self.amount} {self.currency}'s"
#         else:
#             return f"{self.amount} {self.currency}"

#     def __add__(self, additional_amount):
#         if type(additional_amount) is int:
#             return self.amount + additional_amount
#         elif isinstance(additional_amount, Currency) and self.currency == additional_amount.currency:
#             return self.amount + additional_amount.amount
#         elif isinstance(additional_amount, Currency) and self.currency != additional_amount.currency:
#             return f"Cannot add between Currency type {self.currency} and {additional_amount.currency}"
#         else:
#             return "Wront arg..."
    
#     def __iadd__(self, other):
#         return self.__add__(other)

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)
# print(c1)
# print(int(c1))
# print(repr(c1))
# print(c1 + 5)
# print(c1 + c2)
# print(c1 + c3)
# c1+= 5
# print(c1)
# c1+=int(c2)
# print(c1)

#-------------------------------------------------------------------------------------------------------------

# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn
#-------------------------------------------------------------------------------------------------------------

# ANSWER

# from func import add


# print(add(5, 3))

#-------------------------------------------------------------------------------------------------------------
# 🌟 Exercise 3: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
#-------------------------------------------------------------------------------------------------------------

# ANSWER

# from random import randint
# def random_draft(number):
#     comp_number = randint(1,100)
#     if number == comp_number:
#         print(f"Nice it's the same ({number}) number!")
#     else:
#         print(f"Sorry, not today! Your number = {number} and computer number = {comp_number}.")

# random_draft(55)
# random_draft(55)
# random_draft(55)
# random_draft(55)
# random_draft(55)
# random_draft(55)
# random_draft(55)
# random_draft(55)

#-------------------------------------------------------------------------------------------------------------
# 🌟 Exercise 4: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
#-------------------------------------------------------------------------------------------------------------

# ANSWER

# import secrets
# import string

# res = ""
# for i in range(5):
#     res += ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase))
#     print(res)

#-------------------------------------------------------------------------------------------------------------
# 🌟 Exercise 5 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.
#-------------------------------------------------------------------------------------------------------------

# ANSWER

# from datetime import date, datetime

# actual_datetime = datetime.now()
# print(f"Now is {actual_datetime}")

#-------------------------------------------------------------------------------------------------------------
# Exercise 6 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
#-------------------------------------------------------------------------------------------------------------

# ANSWER

# import datetime

# actual_datetime = datetime.datetime.now()
# january_1st = datetime.datetime(2024,1,1, 00, 00)
# delta = january_1st - actual_datetime

# print(f"Time before 1st January: {delta}")

#-------------------------------------------------------------------------------------------------------------
# Exercise 7 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
#-------------------------------------------------------------------------------------------------------------

# ANSWER

# import datetime
# user_input = tuple(input("Type your birthdate (YYYY/MM/DD):\n").split("/"))
# actual_datetime = datetime.datetime.today()
# your_birthdate = datetime.datetime(int(user_input[0]), int(user_input[1]), int(user_input[2]))
# delta = (actual_datetime - your_birthdate).total_seconds()
# delta = int(delta / 60)
# print(f"You lived total {delta} minutes.")

#-------------------------------------------------------------------------------------------------------------
# Exercise 8 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
#-------------------------------------------------------------------------------------------------------------

# ANSWER

from random import randint
from faker import Faker

fake = Faker("en_US")
users = []
for x in range(randint(10,20)):
    temp = {"name":fake.name(), "adress": fake.address(), "language_code": "en_US"}
    users.append(temp)
    print(temp)