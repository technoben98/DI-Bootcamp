# Challenge 1

# input_string = input("Type word separated by comma:\n")

# def sorting (input_string):
#     list1 = input_string.split(",")
#     new_list = [x for x in sorted(list1)]
#     new_list = ",".join(new_list)
#     print(new_list)

# sorting(input_string)

# Challenge 2

sentence1 = "Margaret's toy is a pretty doll."
sentence2 = "A thing of beauty is a joy forever."
sentence3 = "Forgetfulness is by all means powerless!"
sentence4 = "I'm just check that it use only first"

def longest_word(sentence):
    sentence = sentence.split(" ")
    total_count = 0
    for word in sentence:
        if len(word) > total_count:
            total_count = len(word)
    for word in sentence:
        if len(word) == total_count:
            print(word)
            break
longest_word(sentence1)     # Checking that it works
longest_word(sentence2)     # Checking that it works
longest_word(sentence3)     # Checking that it works
longest_word(sentence4)     # Checking that it works