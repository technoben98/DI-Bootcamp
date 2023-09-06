# Exercise 1

# def calculation(a, b):
#     plus = a+b
#     minus = a-b
#     return plus, minus

# res = calculation(40, 10)
# print(res)

# Exercise 2

# def check_even_or_odd (number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(check_even_or_odd(5))

# Exercise 3

# def check_even_or_odd(numbers):
#     i = 0
#     while i < len(numbers):
#         if numbers[i] % 2 == 0:
#             print(f"{numbers[i]} is even")
#             i += 1
#         else:
#             print(f"{numbers[i]} is odd")
#             i += 1

# numbers = [2, 3, 4, 5, 6, 7, 8, 9]
# check_even_or_odd(numbers)
# check_even_or_odd([2, 5, 6, 9, 15, 23])

# Exercise 4

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# def say_hello(people):
#     if len(people) <= 4:
#         print(f"Hello {people}")
# filtered = filter(say_hello, people)
# print(list(filtered))

# Exercise 5

# age = 25
# destination = "Kyiv"
# def get_price_car():
#     if age >= 40:
#         return 200
#     else:
#         return 300

# def get_price_flight():
#     if destination == "Paris":
#         return 400
#     else:
#         return 600
    
# def get_total_price():
#     total = get_price_car() + get_price_flight()
#     return total

# print(get_total_price())

