# Exercise 1

# colors_tuple = ('cyan', 'yellow', 'blue', 'green', 'magenta')

# def colorize(text, color):
#     try :
#         if color not in colors_tuple:
#             raise Exception("wrong color")
#         else:
#             print(text + " " + color)
#     except TypeError as error:
#         print("Wrong type")
#     except Exception as error:
#         print("The error is", error)
# colorize("25", "black")
# colorize(25, "cyan")
# colorize("My text is", "cyan")

# Exercise 2
import os

with open("nameslist.txt") as txt:
    print(txt.readlines())