your_number = input("Please input number from 1 to 100: ")


if int(your_number) % 3 == 0 and int(your_number) % 5 == 0:
    print("FizzBuzz")
elif int(your_number) % 3 == 0:
    print("Fizz")
elif int(your_number) % 5 == 0:
    print("Buzz")
else:
    print("Not this time")