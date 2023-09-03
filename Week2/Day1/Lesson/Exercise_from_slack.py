# Exercise1
miles = input("Put number of miles to convert it to kilometers: \n")
kilometers = float(miles) * 1.61
print(f"{miles} miles - it is {kilometers} kilometers")

# Exercise2

name = 'John Doe'
name_length = int(len(name))
if name_length > 20:
    print(f"Name " + name + " is more than 20 chars long")
    length_description = 'long'
elif name_length > 15:
    print(f"Name " + name + " is more than 15 chars long")
    length_description = 'semi long'
elif name_length > 10:
    print(f"Name " + name + " is more than 10 chars long")
    length_description = 'semi long'
elif name_length >= 8 and name_length <= 10:
    print(f"Name " + name + " is 8, 9 or 10 chars long")
    length_description = 'semi short'
else:
    print(f"Name " + name + " is a short name")
    length_description = 'short'

# Exercise3

number_of_guests = input("Please put your number of guests: \n")
if int(number_of_guests) > 200:
    print("It will cost $20000")
elif int(number_of_guests) <= 200 and int(number_of_guests) > 100:
    print("It will cost $15000")
elif int(number_of_guests) <= 100 and int(number_of_guests) > 50:
    print("It will cost $10000")
else:
    print("It will cost $4000")