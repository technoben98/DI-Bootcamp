# Challenge 1

# word = list(input("Type a word: \n"))
# letters = {}
# temp_values = []
# temp_keys = []
# for i, value in enumerate(word):
#     if value not in letters.keys():
#         temp_values.append(i)
#         letters.update({value : [i]})
#         temp_values.clear()
#     elif value in letters.keys():
#         temp = letters[value]
#         temp.append(i)
# print(letters)


# Challenge 2

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
# wallet = "$300"
# wallet = int(wallet.replace("$", ""))
# my_items = []
# for item, price in items_purchase.items():
#     price_temp = int(price.replace("$", "").replace(",", ""))
#     if int(price_temp) <= int(wallet):
#         my_items.append(item)
#         wallet -= price_temp
# print(my_items)


# ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

# wallet = int(wallet.replace("$", ""))
# my_items = []
# for item, price in items_purchase.items():
#     price_temp = int(price.replace("$", "").replace(",", ""))
#     if int(price_temp) <= int(wallet):
#         my_items.append(item)
#         wallet -= price_temp
# if len(my_items) == 0:
#     print("Nothing")
# else:
#     print(my_items)

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 

# wallet = int(wallet.replace("$", ""))
# my_items = []
# for item, price in items_purchase.items():
#     price_temp = int(price.replace("$", "").replace(",", ""))
#     if int(price_temp) <= int(wallet):
#         my_items.append(item)
#         wallet -= price_temp
# if len(my_items) == 0:
#     print("Nothing")
# else:
#     print(my_items)