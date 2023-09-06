# Exercises 1,2,3

# birthday = {
#     "Vasya" : "1994/04/26", 
#     "Dima" : "1998/05/01",
#     "Vanya" : "2003/04/22",
#     "Ura" : "2000/11/23",
#     "Max" : "1997/01/12"
#     }
# print("You can look up the birthdays of the people in the list!")
# print(birthday.keys())
# new_name = input("Type your name:\n")
# new_date = input("Type your date(YYYY/MM/DD):\n")
# birthday.update({new_name:new_date})
# name = input("Choose name: \n")
# if name in birthday.keys():
#     print(f"{name} birtday is {birthday[name]}")
# else:
#     print(f"Sorry, we don’t have the birthday information for {name}")

# Exercise 4

# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# for item, price in items.items():
#     print(f"The price of {item} is ${price}")

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0
for item in items.values():
    total_cost += item["price"] * item["stock"]
print(f"The total cost to buy everything in stock is ${total_cost}")