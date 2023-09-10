# -----------------------------------------------------------------------------------
# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

# -----------------------------------------------------------------------------------

# ANSWER

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cats = []

# first_cat = Cat("Dee-dee", 9)
# cats.append(first_cat)
# second_cat = Cat("Merci", 8)
# cats.append(second_cat)
# third_cat = Cat("Bender", 15)
# cats.append(third_cat)

# def find_oldest_class (object):
#     oldest_cat = Cat("", 0)
#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     print(f"Oldest cat is {oldest_cat.name}. He is {oldest_cat.age} years old.")

# find_oldest_class(cats)



# -----------------------------------------------------------------------------------
# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
# -----------------------------------------------------------------------------------
# ANSWER


# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark (self):
#         print(f"{self.name} goes woof!")

#     def jump (self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")


# davids_dog = Dog("Rex", 50)
# print(f"David's dog name is {davids_dog.name}. His height is {davids_dog.height}")
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog = Dog("Teacup", 20)
# print(f"Sarah's dog name is {sarahs_dog.name}. His height is {sarahs_dog.height}")
# sarahs_dog.bark()
# sarahs_dog.jump()
# if sarahs_dog.height > davids_dog.height:
#     print(f"{sarahs_dog.name} is bigger.")
# else:
#     print(f"{davids_dog.name} is bigger.")


# -----------------------------------------------------------------------------------
# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

# -----------------------------------------------------------------------------------

# ANSWER

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = list(lyrics)
    
#     def sing_me_a_song(self):
#         # self.lyrics = "".split(",")
#         for value in self.lyrics:
#             print(value)
# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

# -----------------------------------------------------------------------------------

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

# -----------------------------------------------------------------------------------

# ANSWER

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animals (self, new_animal):
        if new_animal not in self.animals:
            for animal in new_animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        for animal in animal_sold:
            self.animals.remove(animal)

    def sort_animals(self):
        self.animals.sort()
        grouped_list = []
        current_group = []

        for animal in self.animals:
            if len(current_group) == 0: 
                current_group.append(animal) 
            else:
                if animal[0] == current_group[0][0]:
                    current_group.append(animal)
                else:
                    grouped_list.append(current_group)
                    current_group = [animal]
        grouped_list.append(current_group)
        self.animals = grouped_list

    def get_group (self):
        for index, value in enumerate(self.animals):
            print(f"Group {index+1}: {value}")

ramat_gan_safari = Zoo ("safari")
new_animals = ["Giraffe", "Cat", "Lion", "Tiger", "Baboon", "Bear", "Coufar", "Eel", "Emu", "Ape"]
ramat_gan_safari.add_animals(new_animals)
ramat_gan_safari.add_animals("Giraffe")
ramat_gan_safari.get_animals()
animal_sold = ["Lion", "Giraffe"]
ramat_gan_safari.sell_animal(animal_sold)
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_group()