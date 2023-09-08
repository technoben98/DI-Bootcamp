input_sentence = input("Type your sentence:\n")
input_sentence = input_sentence.split(" ")
reversed_sentence = []
for value in input_sentence:
    reversed_sentence.insert(0, value)
sentence = " ".join(reversed_sentence)
print(sentence)