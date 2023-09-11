# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

# -----------------------------------------------------------------------------------------------------------------------

# ANSWER

import dog
from random import randint

class PetDog (dog.Dog):
    def __init__(self, name, age, weight, trainded = False):
        super().__init__(name, age, weight)
        self.trained = trainded

    def train(self):
        self.trained = True
        print (self.bark())
    
    def play(self, *other_dogs):
        dogs_list = []
        for dog in other_dogs:
            dogs_list.append(dog.name)
        dogs_list = " and ".join(dogs_list)
        print(f"{self.name} and {dogs_list} all play together.")

    def do_a_trick(self):
        if self.trained == True:
            index = randint(0, 3)
            tricks_list = [f"{self.name} does a barrel roll.",
            f"{self.name} stands on his back legs.",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead."]
            print(tricks_list[index])
        else:
            print(f"{self.name} is not trained.")


dog1 = PetDog("Kuku", 8, 50, False)
dog2 = PetDog("Nana", 8, 50, True)
dog3 = PetDog("Nara", 8, 50, False)

dog1.play(dog2, dog3)
dog3.do_a_trick()
dog3.train()
dog3.do_a_trick()