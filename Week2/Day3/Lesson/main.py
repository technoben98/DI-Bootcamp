# exercise 1

# prices = {
#     "apple" : 2,
#     "banana" : 5,
#     "orange" : 1
# }
# total = sum(prices.values())
# print(total)

# for value in prices.values():
#     total+=value
# print(total)

# user_fruit = input("what fruit do you want?")
# print(f"Your price {prices[user_fruit]}")

# ask the user for the fruit he wants
# depending on the fruit we show him the price
# don't use conditionals

# exercise 2

# create a new list that only contains the uppercased words
# words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']

# words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
# words2 = [word for word in words if word.isupper()]
# print(words2)


# Exercise 3
# Print the total duration of the playlist

# playlist = {
#     'title': "Hello World",
#     'author': "Planet",
#     'songs': [
#         {
#             'song_title': "Song One",
#             'artist': ['Artist 1', 'Artist 2'],
#             'duration': 4.31,
#         },
#         {
#             'song_title': "Song Two",
#             'artist': ['Artist 1'],
#             'duration': 2.53,
#         },
#         {
#             'song_title': "Song Three",
#             'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
#             'duration': 3.43,
#         }
#     ]
# }
# # print(type(playlist))
# # duration = playlist['songs']['duration']
# # print(sum(duration))
# total_duration = 0
# for music in playlist['songs'] :
#     total_duration += music ['duration']
# print(total_duration)
# print(playlist['songs'][0]['duration'])

# fruits = ["apple", "pear", "banana"]
# for index, value in enumerate(fruits):
#     fruits[index] += "s"
# print(fruits)

# Exercise 4

