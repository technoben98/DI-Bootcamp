import random

list_of_numbers = [random.randint(0, 10000) for i in range(20000)]
target_number = 3728

count = 0
for i in range(len(list_of_numbers)):
    for j in range(i+1, len(list_of_numbers)):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            count += 1

print(f"Number of pairs that sum up to {target_number} : , {count}")