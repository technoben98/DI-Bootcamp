# Exercise 1

# list1 = []
# def insert_to_list (list_name, value, position):
#     position -=1
#     if position > len(list_name):
#         for index in range(position):
#             list_name.insert(index, "")
#     list_name.insert(position, value)
#     print(list_name)

# insert_to_list(list1, "hi", 7)

# Exercise 2

# def find_count_of_spaces(text):
#     count = 0
#     for i in text:
#         if i == " ":
#             count +=1
#     print(count)
# find_count_of_spaces("How much spaces here?")

# Exercise 3

# def find_number_of_upper_and_lower(text:str):
#     lower = 0
#     upper = 0
#     for i in text:
#         if i.islower():
#             lower += 1
#         elif i.isupper():
#             upper +=1
#     print(f"In this text: \n{upper} upper case letters \n{lower} lower case letters")

# find_number_of_upper_and_lower("HOW much LeTTers")

# Exercise 4

# def my_sum(list_numbers):
#     list_sum = 0
#     for i in list_numbers:
#         list_sum += i
#     return list_sum
# print(my_sum([1,5,4,2]))

# Exercise 5

# def max_number(list_numbers):
#     max_number = 0
#     for i in list_numbers:
#         if i > max_number:
#             max_number = i
#     return max_number
# print(max_number([0,70,3,50]))

# Exercise 6
# def factorial(number):
#     factorial = 1
#     for i in range(2,number+1):
#         factorial = factorial*i
#     print(factorial)
# factorial(5)

# Exercise 7

# def count(any_list, obj):
#     count = 0
#     for i in any_list:
#         if i == obj:
#             count+=1
#     return count
# print(count(['a','a','t','o'],'a'))

# Exercise 8

# import math

# def norm(lst):
#     sum_of_squares = sum([x**2 for x in lst])
#     result = math.sqrt(sum_of_squares)
#     return int(result)

# print(norm([1,2,2]))

# Exercise 9

# def is_monotonic(arr): 
#     is_increasing = True
#     is_decreasing = True
    
#     for i in range(1, len(arr)):
#         if arr[i] < arr[i-1]:
#             is_increasing = False
#         if arr[i] > arr[i-1]:
#             is_decreasing = False
        
#     return is_increasing or is_decreasing

# print(is_monotonic([7,6,5,5,2,0]))
# print(is_monotonic([2,3,3,3]))
# print(is_monotonic([1,2,0,4]))

# Exercise 10

# def longest_word(words_list):
#     longest_word = ''
#     for i in words_list:
#         if len(i) > len(longest_word):
#             longest_word = i
#     return longest_word

# print(longest_word(["Radar", "home", "literal"]))

# Exercise 11

# def sorting(unsorted_list):
#     int_list = []
#     str_list = []
#     for i in unsorted_list:
#         if isinstance(i, int):
#             int_list.append(i)
#         elif isinstance(i,str):
#             str_list.append(i)
#     return int_list, str_list

# print(sorting([1, 2, "home", "three", 5, "nice"]))

# Exercise 12

# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
    
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
    
#     return True
# print(is_palindrome('radar'))
# print(is_palindrome("john"))

# Exercise 13

# def sum_over_k(sentence, k):
#     sentence = sentence.split(' ')
#     count = 0
#     for i in sentence:
#         if len(i) > k:
#             count+=1

#     return count
# sentence = 'Do or do not there is no try'
# print(sum_over_k(sentence, 2))

# Exercise 14

# def dict_avg(dictionary):
#     sum_of_values = 0
#     count = 0
#     for key in dictionary:
#         sum_of_values += dictionary[key]
#         count+=1
#     return int(sum_of_values/count)

# print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))

# Exercise 15

# def common_divisors(num1, num2):
#     divisors = []
#     for i in range(2, num1 + 1):
#         if num1 % i == 0:
#             divisors.append(i)
    
#     common_divisors = []
#     for divisor in divisors:
#         if num2 % divisor == 0:
#             common_divisors.append(divisor)
    
#     return common_divisors

# print(common_divisors(10,20))

# Exercise 16

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

# print(is_prime(11))
# print(is_prime(12))

# Exercise 17

# def weird_print(list_numbers):
#     new_list = []
#     for index, value in enumerate(list_numbers):
#         if value % 2 == 0:
#             if index % 2 == 0:
#                 new_list.append(value)
#     return new_list

# print(weird_print([1,2,2,3,4,5]))

# Exercise 18

# def type_count(**kwargs):
#     count = {}
#     for arg in kwargs.values():
#         t = type(arg).__name__
#         count[t] = count.get(t, 0) + 1
#     return count

# result = type_count(a=1, b='string', c=1.0, d=True, e=False)
# for k, v in result.items():
#     print(f"{k}: {v}")

# Exercise 19

# def custom_split(string, delimiter=" "):
#     temp_word = []
#     splited_list = []
#     for i in string:
#         if i != delimiter:
#             temp_word.append(i)
#         elif i == delimiter:
#             temp_word = ''.join(temp_word)
#             splited_list.append(temp_word)
#             temp_word = []
#     temp_word = ''.join(temp_word)
#     splited_list.append(temp_word)
#     string = splited_list
#     return string

# print(custom_split("Hello world, how are you?", " "))
# print(custom_split("apple,banana,cherry", ","))

# Exercise 20

def hide_password(): 
    password = input("Type your password:\n")
    return '*' * len(password)

print(hide_password())