import random

# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

# list_a = [0, 1, 2, 3, 4]
# list_b = [5, 6, 7, 8, 9]
# list_a.extend(list_b)
# print(list_a)


# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

# index = 1500
# while index < 2500:
#     if index % 5 ==0 or index % 7 ==0:
#         print(index)
#         index+=1
#         continue
#     else:
#         index+=1
#         continue


# Exercise 3: Check The Index
# Instructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# while True:
#     name = input("Type your name or 'exit':\n")
#     if name == "exit":
#         break
#     else:
#         if name in names:
#             print(names.index(name))
#             break
#         else:
#             print("Try another name.")
#             continue



# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87

# first = int(input("First number:\n"))
# second = int(input("Second number:\n"))
# third = int(input("Third number:\n"))
# greatest = 0
# if first > second and first > third:
#     greatest = first
# elif second > third and second > first:
#     greatest = second
# elif third > first and third > second:
#     greatest = third
# else:
#     greatest = first
#     print("It's the same numbers!")
# print(f"The greatest number is: {greatest}.")



# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# vowels = ["a", "e", "i", "o", "u"]
# for char in alphabet:
#     print(char)
#     if char in vowels:
#         print("This is vowel letter.")
#         continue
#     else:
#         print("This is consonant letter.")
#         continue



# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

# index = 0
# words = []
# word_index = 0
# while index < 7:
#     words.append(input("Type a word: \n"))
#     index+=1
# letter = input("Type a letter:\n")
# for word in words:
#     if letter in word:
#         word_index = words.index(word)
#         print(f"{word_index}/{word.index(letter)}")
#         continue
#     else:
#         print(f"Nice try to find '{letter}' in '{word}' :)")
#         continue
# print(words) 



# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

# number_list = []
# i = 1
# while i <= 1000000:
#     number_list.append(i)
#     i+=1
# print(min(number_list))
# print(max(number_list))
# print(sum(number_list))


# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# string = input("Type your numbers")
# list_1 = string.split(", ")
# tuple_1 = tuple(string.split(", "))
# print(list_1)
# print(tuple_1)


# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

wins = 0
loses = 0
total = 0
while True:
    user_number = int(input("Type your number (from 1 to 9) (For exit type '0')"))
    python_number = random.randint(1, 9)
    if user_number == python_number:
        print(f"You win! Your number '{user_number}' and my number '{python_number}!'")
        wins +=1
        total +=1
        continue
    if user_number == 0:
        print(f"Thank you for playing. You played '{total}' games.\n Wins: {wins}\n Loses: {loses}")
        break
    else:
        print("You lose. Try again!")
        loses+=1
        total+=1
        continue
