# exercise

# class Dog :

#     def __init__(self, dog_name, dog_age, dog_color = "black", energy = 100) :
#         self.name = dog_name
#         self.age = dog_age
#         self.color = dog_color
#         self.energy = 100
#         # nb energypoints

#     # method happybirthday increment the age by one
#     def happy_birthday(self) :
#         self.age += 1

#     def show_info (self) :
#         print(f"The dog name is {self.name}, his age is {self.age}, he is of color {self.color}")

#     def go_to_groomer(self, owner_color) :
#         self.color = owner_color


#     def play (self, activity) :
#         if self.energy > 10: #if energy is more than 10
#             if activity == "ball" and self.energy >= 10: # if we choose ball and have enought energy
#                 self.energy -= 10 # decrise energy by 10
#                 print(f"I'm playing with ball!") # print message
#             elif activity == "frisbee" and self.energy >=30: # if we choose frisbee and have enought energy
#                 self.energy -= 30 # decrise energy by 30
#                 print(f"I'm playing with frisbee!") # print message
#             elif isinstance(activity, Dog) and self.energy >= 70: # if we choose another dog and have enought energy
#                 self.energy -= 70 # decrise energy by 70
#                 activity.energy -= 70 # decrise another dog energy by 70
#                 print(f"We are playing together with {activity.name}") # print message
#             else: # if we have not enought energy go sleep
#                 self.sleep()
#         else: # if we have less than 10 energy dog goes sleep too
#             self.sleep()
    
#     def sleep(self):
#         print("I'm sleeping")
#         self.energy = 100
            


# lea_dog = Dog("Spock", 2)
# # lea_dog.go_to_groomer("pink")
# # lea_dog.show_info()
# # # print(lea_dog.__dict__)

# dan_dog = Dog("Rex", 4, "white")
# # # print(dan_dog.__dict__)
# # dan_dog.show_info()

# print(lea_dog.energy)
# lea_dog.play("ball")
# # lea_dog.play("frisbee")
# lea_dog.play(dan_dog)
# print(lea_dog.energy)
# print(dan_dog.energy)


# Exercise 2

# Basic Classes
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary

# 1. Create 2 users object and display their attribute
# - Lea Smith 30 years old developer 25000 shekels
# - David Schartz 20 years old project manager 20000 shekels

# 2. Add those methods to the class
# - get_fullname(self) : that return the firstname + lastname
# - (self) : that return the age incremented by one
# - get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# - show_info(self) : that will print the information of the employee --> name, age, job, salary

# 3. Call all the methods on the 2 objects

class Employee :
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def get_fullname (self):
        full_name = self.firstname + " " + self.lastname
        return full_name
    
    def get_new_age(self):
        self.age += 1 
    
    def get_promotion(self, promotion_amount):
        self.salary = self.salary + promotion_amount
    
    def show_info(self):
        print(f"My name is {self.get_fullname()}. I'm {self.age} years old. I work like {self.job}. My salary is {self.salary}.")
    
first_employee = Employee("Lea", "Smith", 30, "developer", 25000)
second_employee = Employee("David", "Schartz", 20, "manager", 20000)

first_employee.get_fullname()
second_employee.get_fullname()
first_employee.get_new_age()
second_employee.get_new_age()
first_employee.get_promotion(2300)
second_employee.get_promotion(4600)
first_employee.show_info()
second_employee.show_info()