# Exercise 1

list1 = []
def insert_to_list (list_name, value, position):
    position -=1
    if position > len(list_name):
        for index in range(position):
            list_name.insert(index, "")
    list_name.insert(position, value)
    print(list_name)

insert_to_list(list1, "hi", 7)