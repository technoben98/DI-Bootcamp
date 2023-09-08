cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = []
cars_list = cars_string.split(", ")
print(len(cars_list))
cars_list.sort()
for i,v in enumerate(cars_list):
    print(cars_list[4-i])
new_list = [value for index, value in enumerate(cars_list) if "o" in value]
print(new_list)
new_list = [value for index, value in enumerate(cars_list) if "i" in value]
print(new_list)

second_cars_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
second_cars_list =  set(second_cars_list)
second_cars_list = list(second_cars_list)
second_string = ", ".join(second_cars_list)
print(second_string)

second_cars_list.sort()
print(second_cars_list)
another_list = []
for index, value in enumerate(second_cars_list):
    another_list.append(value[::-1]) 
print(another_list)