import random

line = input("Put here your string: \n")
answer = 0
while answer !=1:
    if int(len(line)) < 10:
        answer = 0
        print("string not long enough")
        line = input("Put here your string: \n")
    elif int(len(line)) > 10:
        answer = 0
        print("string too long")
        line = input("Put here your string: \n")
    elif int(len(line)) == 10:
        answer = 1
        print("perfect string")
        temp_list = list(line)
        print(temp_list[0] + temp_list[9])
        new_line = ""
        for index in range(len(temp_list)):
                    letter = temp_list[index]
                    new_line += letter
                    index += 1
                    print(new_line)
random.shuffle(temp_list)
crazy =''.join(temp_list)
print(crazy)