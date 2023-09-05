# Challenge 1

# number = int(input("Type your number: \n"))
# lenth = int(input("Type your lenth: \n"))
# number_list = []
# new_number = 0
# while len(number_list) < lenth: 
#     new_number = new_number + number
#     number_list.append(new_number)
#     continue
# print(number_list)

# Challenge 2

word = input("Your word:\n")
new_word = []
prev_letter = " "
current_letter = " "
for i in word :
    current_letter = i
    if current_letter != prev_letter:
        new_word.append(current_letter)
        prev_letter = i
print(''.join(new_word))