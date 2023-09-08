# Exercise 1

# def get_full_name(first_name="", middle_name="", last_name=""):
#     if middle_name:
#         full_name = f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
#     else:
#         full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
#     return full_name

# print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
# print(get_full_name(first_name="bruce", last_name="lee"))



# Exercise 2

# morze = {'a': '*—', 'b': '—***', 'c': '—*—*', 'd': '—**',   
#          'e': '*', 'f': '**—*', 'g': '——*', 'h': '****',
#          'i': '**', 'j': '*———', 'k': '—*—', 'l': '*—**',
#          'm': '——', 'n': '—*', 'o': '———', 'p': '*——*',
#          'q': '——*—', 'r': '*—*', 's': '***', 't': '—',
#          'u': '**—', 'v': '***—', 'w': '*——', 'x': '—**—',
#          'y': '—*——', 'z': '——**', ' ' : '/'}

# choise = True

# def get_input_text():
#     text_to_convert = input("Type your text to convert:\n")
#     text_to_convert.lower()
#     return text_to_convert

# def convert_to_morze_or_from():
#     to_or_from = int(input("Choose to morze(0) or from morze(1)"))
#     global choise
#     if to_or_from == 0:
#         choise = True
#     elif to_or_from == 1:
#         choise = False
#     else:
#         print("Not right!")

# def convert_to_morze():
#     text_to_convert = get_input_text()
#     morze_text = []
#     for char in text_to_convert:
#         morze_text.append(morze[char])
#     print(" ".join(morze_text))

# def start():
#     convert_to_morze_or_from()
#     if choise == True:
#         convert_to_morze()
#     else:
#         convert_from_morze()

# morze_to_latin = {value: key for key, value in morze.items()}

# def convert_from_morze():
#     text_to_convert = get_input_text().split(" ")
#     text_from_morze = []
#     for value in text_to_convert:
#         text_from_morze.append(morze_to_latin[value])
#     print("".join(text_from_morze))

# start()


# Exercise 3

def box_printer(*string):
    max_lenth = 0
    for value in string:
        if max_lenth < len(value):
            max_lenth = len(value)
    
    max_lenth += 4
    print("*"*max_lenth)
    max_lenth -=4
    for value in string:
        print(f"* {value:{max_lenth}} *")
    max_lenth += 4
    print("*"*max_lenth)

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
    
    
# Exersice 4

# This code sorting numbers in list from smallest to biggest

# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)