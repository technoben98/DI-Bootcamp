# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

# -----------------------------------------------------------------------------------------------------------------------
# ANSWER

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     pass

# bengal_1 = Bengal("Tuti", 4)
# chartreux_1 = Chartreux("Rys'", 5)
# siamese_1 = Siamese("Lily", 2)
# all_cats = [bengal_1, chartreux_1, siamese_1]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

# -----------------------------------------------------------------------------------------------------------------------

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

# -----------------------------------------------------------------------------------------------------------------------

# ANSWER

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."
    
    def run_speed(self):
        speed = self.weight / self.age * 10
        return speed
    
    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f"{self.name} won the fight with {self.run_speed()*self.weight} speed"
        else:
            return f"{other_dog.name} won the fight with {other_dog.run_speed()*other_dog.weight} speed"
        
# dog1 = Dog("Kuku", 10, 60)
# dog2 = Dog("Nana", 8, 50)
# dog3 = Dog("Jerry", 12, 80)

# print(dog1.fight(dog2))
# print(dog2.fight(dog3))
# print(dog3.fight(dog1))

# -----------------------------------------------------------------------------------------------------------------------