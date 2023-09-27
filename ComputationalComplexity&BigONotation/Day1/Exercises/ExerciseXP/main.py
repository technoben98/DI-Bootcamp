# 🌟 Exercise 1: Identifying Time Complexity
# Instructions
# Identifying the Time Complexity for each of the below programs
# ========================================================================================================================================================================

# Snippet 1

# for i in range(10):
#     print(i)
# ANSWER
# The time complexity of Snippet 1 is O(1) because it contains a fixed number of iterations (10) regardless of the input size.

# Snippet 2

# for i in range(n):
#     for j in range(n):
#         print(i, j)
# ANSWER
# The time complexity of Snippet 2 is O(n^2) because it contains nested loops that iterate from 0 to n, resulting in a total of n * n iterations.


# Snippet 3

# i = 1
# while i < n:
#     i *= 2
#     print(i)
# ANSWER
# The time complexity of Snippet 3 is O(log n) because the variable i doubles in value with each iteration of the while loop until it reaches or exceeds the value of n. This doubling behavior corresponds to a logarithmic time complexity.

# ========================================================================================================================================================================
# 🌟 Exercise 2: Understanding Insertion Sort
# Instructions
# Insertion Sort is an in-place, stable sorting algorithm that works in a manner similar to sorting a hand of playing cards. It sorts the array by moving each element to its correct position in the sorted part of the array.

# insertion_sort

# Algorithm Explanation

# Start from the second element (index 1), assume the element at index 0 is sorted.
# Compare the current element with the previous elements.
# If the current element is smaller than the previous element, move the previous element to the right.
# Repeat the process until the correct position for the current element is found and then insert it.
# Continue the process for each of the elements in the unsorted section of the array.


# Simple Example

# Consider an array [5, 2, 9, 1, 5, 6]:

# Start with the second element 2. 2 < 5, so swap them: [2, 5, 9, 1, 5, 6]
# Next, take 9. It’s already in the right position: [2, 5, 9, 1, 5, 6]
# Take 1. Move 9 and 5 to the right and insert 1: [1, 2, 5, 9, 5, 6]
# Take 5. Move 9 to the right and insert 5: [1, 2, 5, 5, 9, 6]
# Finally, take 6. Move 9 to the right and insert 6: [1, 2, 5, 5, 6, 9]
# The array is now sorted.

# Complexity

# Best-case time complexity: O(n) when the array is already sorted.
# Average-case time complexity: O(n^2)
# Worst-case time complexity: O(n^2) when the array is sorted in reverse order.
# Space complexity: O(1) (In-place)


# Rules

# Insertion sort is stable; it does not change the relative order of equal elements.
# It’s an in-place algorithm; it sorts the array by making changes within the array itself.
# It’s adaptive, meaning it becomes faster if the array is partially sorted.


# Your task is to implement this algorithm in Python and understand its performance characteristics.
# You can use the following starting point:



# numbers = [5, 2, 9, 1, 5, 6]

# def insertion_sort(numbers: list) -> None:
#    pass

# insertion_sort(numbers) # sorts the numbers list
# print(numbers) # check that the sorting is successfull
# ========================================================================================================================================================================

# numbers = [5, 2, 9, 1, 5, 6]

# def insertion_sort(numbers: list) -> None:
#    # Start from the second element (index 1)
#     for i in range(1, len(numbers)):
#         # Assume the element at index 0 is sorted
#         key = numbers[i]
#         j = i - 1
#         # Compare the current element with the previous elements
#         while j >= 0 and key < numbers[j]:
#             # If the current element is smaller than the previous element,
#             # move the previous element to the right
#             numbers[j + 1] = numbers[j]
#             j -= 1
#         # Insert the current element at the correct position
#         numbers[j + 1] = key

# insertion_sort(numbers) # sorts the numbers list
# print(numbers) # check that the sorting is successfull

# ========================================================================================================================================================================
# 🌟 Exercise 3: Understanding Binary Search
# Instructions
# Binary Search is an efficient algorithm for finding a target value within a sorted array. Unlike linear search, which checks each element in order, binary search divides the array in half and eliminates half of the remaining elements in each iteration.



# binary_search



# Algorithm Explanation

# Ensure that the array is sorted.
# Define three pointers: low, high, and mid. Initialize low at index 0 and high at the last index of the array.
# Calculate mid as the average of low and high.
# Compare the mid-element with the target.
# If it’s equal, return the index of mid.
# If it’s less, update low = mid + 1 and continue.
# If it’s more, update high = mid - 1 and continue.
# If low exceeds high, the target is not in the array.


# Simple Example

# Consider a sorted array [1, 3, 5, 7, 9, 11] and you want to find the index of 7:

# low = 0, high = 5, mid = 2
# arr[mid] = 5 < 7 so low = mid + 1 = 3
# low = 3, high = 5, mid = 4
# arr[mid] = 9 > 7 so high = mid - 1 = 3
# low = 3, high = 3, mid = 3
# arr[mid] = 7 is the target, so return mid = 3


# Complexity

# Best-case time complexity: O(1) when the target is in the middle of the array.
# Average-case time complexity: O(log n)
# Worst-case time complexity: O(log n)
# Space complexity: O(1) (In-place)


# Rules

# Binary search only works on sorted arrays.
# It’s an in-place algorithm; it doesn’t require extra space to operate, aside from variables for the pointers.
# It can return incorrect results on non-distinct arrays if you’re not careful about updating low and high.


# Your task is to implement this algorithm in Python and understand its performance characteristics.
# You can use the following starting point:



# numbers = [1, 3, 5, 7, 9, 11]

# def binary_search(numbers: list, value: int) -> int:
#    pass

# binary_search(numbers, 7) # returns 3
# ========================================================================================================================================================================

# ANSWER

numbers = [1, 3, 5, 7, 9, 11]

def binary_search(numbers: list, value: int) -> int:
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    print (f"{value} not in list!")


binary_search(numbers, 7) # returns 3
result = binary_search(numbers, 7)
print(result)