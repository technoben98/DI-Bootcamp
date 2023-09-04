# # Exercise1

# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[list1.index(20)] = 200
# print(list1)

# # Exercise 2

# user_answer = input("Give me an index and a new object separated by coma:\n")
# print("You choose: " + user_answer)
# list1 = ["computer", "phone", "headphones"]
# user_list = user_answer.split(", ")
# print(user_list)
# list1.insert(int(user_list[0]), user_list[1])
# print(list1)

# Exercise 3

# a_tuple = (10, 20, 30, 40)
# a, b, c, d = a_tuple
# print(a)
# print(b)
# print(c)
# print(d)

# Exercise 4

# user_number = int(input("Put your number: \n"))
# for i in range(11):
#     print(f"{user_number} x {i} = " + f"{user_number*i}")

# Exercise 5

# index = 1
# while index < 11:
#     print(index)
#     index +=1

# Exercise 6

# for num in range(15):
#     if num % 2 == 0:
#         print(f"The number {num} is even")
#     else:
#         print(f"The number {num} is odd")

# Exercise 7

# price_restaurant = [20, 31.4, 27.8]
# total = 0
# for num in price_restaurant:
#     total = total + num
# print(total)

# Exersice 8

# words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
# words2 = []
# print(words2)
# for word in words:
#     if word.isupper():
#         words2.append(word)
# print(words2)

# Exercise 9

bank_amount = 10000
computer_price = 2000
count = 0

while bank_amount >= computer_price:
    print("I buy a computer")
    bank_amount -= computer_price
    count += 1
print(count)