import math
# Exercise 1


# c = 50
# h = 30
# d = 0
# string = input("Type a numbers(','): \n")
# string = string.split(",")
# numbers_list = []
# squares_list = []
# i = 0
# while i <= 2:
#     numbers_list.append(int(string[i]))
#     i+=1
# z = 0
# while z < len(numbers_list):
#     d = numbers_list[z]
#     q = math.sqrt((2*c*d)/h)
#     squares_list.append(int(q))
#     z+=1
#     continue
# print(squares_list)

# Exercise 2
import math

number_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
# print(number_list)
# # number_list.sort()
# # print(number_list)
# print(sum(number_list))
# first_and_last = [number_list[0], number_list[-1]]
# print(first_and_last)
# more_than_50 = []
# i = 0
# while i < len(number_list):
#     if number_list[i] >= 50:
#         more_than_50.append(number_list[i])
#         i+=1
#         continue
#     else:
#         i+=1
#         continue
# i = 0
# print(more_than_50)
# less_than_10 = []
# while i < len(number_list):
#     if number_list[i] <= 10:
#         less_than_10.append(number_list[i])
#         i+=1
#         continue
#     else:
#         i+=1
#         continue
# print(less_than_10)
# # i = 0
# # squared_numbers = []
# # while i < len(number_list):
# #     math.sqrt
# #     if math.sqrt(number_list[i]) % 1 == 0:
# #         squared_numbers.append(number_list[i])
# #         i+=1
# #         continue
# #     else:
# #         i+=1
# #         continue
# # print(squared_numbers)
# i = 0
# set_without_duplicates = set(number_list)
# without_duplicates = []
# for number in set_without_duplicates:
#     without_duplicates.append(number)
# print(without_duplicates)
# average_of_list = sum(number_list)/len(number_list)
# print(average_of_list)
# print(max(number_list))
# print(min(number_list))

# Bonus:
# i = 0
# total = 0
# largest = 0
# smallest = 50
# while i < len(number_list):
#     temp = number_list[i]
#     total = total + temp
#     i+=1
#     if largest < temp:
#         largest = temp
#     if smallest > temp:
#         smallest = temp
# print(total, largest, smallest)