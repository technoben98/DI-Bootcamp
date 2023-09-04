# Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.


# my_fav_numbers = {1, 3, 5, 9}
# my_fav_numbers.add(6)
# my_fav_numbers.add(12)
# my_fav_numbers.remove
# print(my_fav_numbers)
# my_fav_numbers.remove(12)
# friends_fav_numbers = {3, 7, 8, 9}
# print(friends_fav_numbers)
# our_fav_numbers = my_fav_numbers.union(friends_fav_numbers)
# print(our_fav_numbers)




# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# integers = (2, 3, 4, 5)
# ANSWER
# !Not possible to add somethink to tuple


# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.pop(-1)
# basket.insert(0, "Apples")
# apples = basket.count("Apples")
# basket.clear()
# print(basket)


# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# Integer - is for numbers and float - is for floating point numbers
# float_list = []
# counter = 1.0
# for i in range(8):
#     counter += 0.5
#     float_list.append(counter)
# print(float_list)



# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# for i in range(20):
#     print(i+1)


# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# while True:
#     name = input("Please enter your name: \n")
#     if name != "Dmitriy":
#         print("Try again!")
#         continue
#     elif name == "Dmitriy":
#         print("Nice! You have a same name!")
#         break
                 


# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# fruits = input("Please type your favourite fruits with space:\n")
# fruits_list = fruits.split(" ")
# user_answer = input("Please type and fruit:\n")
# if user_answer in fruits_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")


# 🌟 Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# toppings = []
# price = 10
# while True:
#     topping = input("Please add your favourite toppings or write \'quit\' to finish:\n")
#     if topping != "quit":
#         print("You added " + topping + " to pizza.")
#         topping += topping
#         price += 2.5
#         continue
#     else:
#         print(f"Thank you. Your total price is: {price}")
#         break




# 🌟 Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


# total_price = 0
# family_size = int(input("How much ticket you need?\n"))
# index = 0
# while index <= family_size-1:
#     age = int(input("How years old your family members?\n"))
#     if age < 3:
#         index+=1
#         continue
#     elif 3 <= age <= 12:
#         total_price += 10
#         index+=1
#         continue
#     elif age > 12:
#         index+=1
#         total_price += 15
# print(f"Your total price is {total_price}.")

# names_list = []
# while True:
#     name = input("Type your name or type 'quit' if you wont finish:\n")
#     if name == "quit":
#         break
#     else:
#         age = int(input("Type your age:\n"))
#         if age > 16 and age < 21:
#             print("Sorry, you cant to go on this movie!")
#             continue
#         else:
#             names_list.append(name)
#             continue
# print(names_list)



# 🌟 Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# while True:
#     if "Pastrami sandwich" in sandwich_orders:
#         sandwich_orders.remove("Pastrami sandwich")
#         continue
#     else:
#         break
# finished_sandwiches = []
# while len(sandwich_orders) > 0:
#     finished = sandwich_orders.pop(0)
#     print(f"I made your " + finished)
#     finished_sandwiches.append(finished)
#     continue
# print(finished_sandwiches)