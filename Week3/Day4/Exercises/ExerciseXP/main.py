# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
# ---------------------------------------------------------------------------------------------------------------------------------

# ANSWER

# import random

# words_list = []
# path = "D:\DI-Bootcamp\Week3\Day4\Exercises\ExerciseXP\\norvig.com_ngrams_sowpods.txt"
# def get_words_from_file(path):
#     with open(path, "r") as txt:
#         global words_list
#         words_list = txt.readlines()

# def get_random_sentence (lenth):
#     sentence = []
#     for _ in range(lenth):
#         sentence.append((random.choice(words_list)).lower())
#     sentence = ''.join(sentence).replace("\n"," ")
#     return sentence

# def main():
#     try:
#         lenth = int(input("Hi, I will generate for you random sentence. Only put here lenth (from 2 to 20) of sentence:\n"))
#         if 2 > lenth > 20: 
#             raise Exception
#     except Exception:
#         print("Wrong number")
#         exit()
#     get_words_from_file(path)
#     print(get_random_sentence(lenth))

# main()


# ---------------------------------------------------------------------------------------------------------------------------------
# 🌟 Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
# ---------------------------------------------------------------------------------------------------------------------------------

# ANSWER

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_dict = json.loads(sampleJson)

salary = json_dict["company"]["employee"]["payable"]["salary"]
print(salary)
json_dict["company"]["employee"]["birth_date"] = "04-01-1996"
print(json_dict["company"]["employee"])
file_path = "output.json"
with open(file_path, "w") as file:
    json.dump(json_dict, file)

print("JSON data saved to file:", file_path)