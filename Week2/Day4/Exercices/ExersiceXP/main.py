# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.


# ANSWER

# def print_message():
#     print("Hi, i'm learning Python")
# print_message()




# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.


#ANSWER

# def favourite_book(title):
#     print(f"One of my favorite books is {title}")
# favourite_book("The Witcher")




# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.


# ANSWER

# def describe_city (city = "Reykjavik", country = "Iceland"):
#     print(f"{city} is in {country}")
# describe_city()
# describe_city("Kyiv", "Ukraine")



# 🌟 Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.


# ANSWER

# import random

# def comparing_answers (user_number = 1):
#     computer_number = random.randint(1, 100)
#     if user_number == computer_number:
#         print("Nice, you right!")
#     else:
#         print(f"It's not that number:\nYour number: {user_number}.\nComputer number: {computer_number}.")
# def gaming_with_user():
#     while True:
#         user_number = int(input("Type your number (for exit type 0)"))
#         comparing_answers(user_number)
#         if user_number == 0:
#             print("Thank you for playing!")
#             break
# gaming_with_user()



# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.


# ANSWER

# def make_shirt(size = "L", text = "I love Python"):
#     print(f"The size of the shirt is {size} and the text is {text}")
# make_shirt()
# make_shirt("M")
# make_shirt("M", "Nice")

# size = "L"
# text = "I love coding"

# make_shirt(size, text)




# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


# ANSWER

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians():
#     for name in magician_names:
#         print(name)

# show_magicians()
# def make_great():
#     i = 0
#     for name in magician_names:
#         magician_names[i] = name + " the Great"
#         i += 1

# make_great()
# show_magicians()




# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


# ANSWER

# import random
# def get_random_temp(season):
#     if season == "winter":
#         temp = random.randint(-10, 10)
#     elif season == "spring":
#         temp = random.randint(-3, 20)
#     elif season == "summer":
#         temp = random.randint(17, 40)
#     elif season == "autumn":
#         temp = random.randint(-2, 20)
#     print(temp)
#     return float(temp)

# def main():
#     user_month = int(input("Type your month number:\n"))
#     user_season = ""
#     if 3 <= user_month <=5:
#         user_season = "spring"
#     elif 6 <= user_month <= 8:
#         user_season = "summer"
#     elif 9 <= user_month <= 11:
#         user_season = "autumn"
#     elif user_month == 12 or user_month < 3:
#         user_season = "winter"

#     temp = get_random_temp(user_season)
#     print(f"The temperature right now is {temp} degrees Celsius.")
#     if temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= temp <= 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif 17 <= temp <= 23:
#         print("It's worth taking something light")
#     elif 24 <= temp <= 32:
#         print("It's time to go out for a walk")
#     elif 33 <= temp <= 40:
#         print("Looks like it's time for air conditioning")
    
# main()





# 🌟 Exercise 5 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.


# ANSWER

import random
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_user():
    count = 0
    wrong_answers = []
    correct_answers = 0
    incorrect_answers = 0
    total_answers = 0
    while count != 5:
        number_of_question = random.randint(0, 5)
        print(data[number_of_question]['question'])
        answer = input("Type your answer:\n")
        if answer == (data[number_of_question]['answer']):
            print("Nice! You are right!")
            correct_answers += 1
            total_answers += 1
            count +=1
        else:
            print("Wrong!")
            incorrect_answers += 1
            total_answers += 1
            count += 1
            wrong_answers.append(answer)
            print(f"Question was:\n{data[number_of_question]['question']}\nYour answer: {answer}\nCorrect answer: {data[number_of_question]['answer']}")
            if incorrect_answers == 3:
                print("")
                yes_or_no = input("You have 3 incorect answers, try again maybe?(Y/N)")
                if yes_or_no == "Y":
                    count = 0
                    total_answers = 0
                    correct_answers = 0
                    incorrect_answers = 0
                    continue
                elif yes_or_no == "N":
                    print("See you.")
                    break
    print(f"Your score:\n Total games = {total_answers}.\n Correct answers = {correct_answers}.\n Incorrect answers = {incorrect_answers}.\nThank you for playing.")
ask_user()