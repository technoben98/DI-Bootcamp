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
for i in word :
    if i not in new_word:
        new_word.append(i)
print(''.join(new_word))