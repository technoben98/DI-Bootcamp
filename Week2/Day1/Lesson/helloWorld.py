# print ("Hello World!")
# number_1 = 5
# number_2 = 6
# print (number_1+number_2)
# print(4+5)
# print(2**3)
# print(type(number_1))

my_age = 25
my_new_age = my_age + 123879
sentence = f"After 123879 years I will be {my_new_age} years old"
print(sentence)

first_name = "Dmitriy"
last_name = "Benevelskyi"

print(first_name + " " + last_name)

print(" New Line")

#integer cars it's number of cars
cars = 100
#float space it's about how many passengers
space_in_a_car = 4.0
#integer driver how many drivers we have
drivers = 30
#integer how many passengers we have
passengers = 90
#integer how many free cars
cars_not_driven = cars - drivers
#integer how many cars using
cars_driven = drivers
#integer how many passengers will be ride today
carpool_capacity = cars_driven * space_in_a_car
#float how many average passengers in one car
average_passengers_per_car = passengers / cars_driven


print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")

# input("Please write your name")
name = input("Please write your name: ")
print("Your name is: " + name)