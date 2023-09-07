sentence = input("Type your sentence:\n")
character = input("Type character:\n")

def find_count_of_char (sentence, character):
    total = 0
    for char in sentence:
        if char == character:
            total += 1
    print(f"Totally in your sentence {total} characters {character}.")

find_count_of_char(sentence, character)