class Text:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_file(cls, path):
        with open(path, "r") as file:
            text = file.read()
        return cls(text)

    def get_word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count > 0:
            return count
        else:
            return None

    def get_most_common_word(self):
        words = self.text.split()
        count = 0
        most_common_word = ""
        for word in words:
            temp_count = words.count(word)
            if temp_count > count:
                most_common_word = word
                count = temp_count
        return most_common_word
                

    
    def get_unique_word(self):
        words = self.text.split()
        unique = []
        for word in words:
            if words.count(word) == 1:
                unique.append(word)
        return unique
    
my_text = Text("Hi i'm very like apples very like oranges with apples and apples")
print(f"You used word 'like' {my_text.get_word_frequency('like')} times")
print(f"Your most common word: {my_text.get_most_common_word()}")
print(f"Unique words: {my_text.get_unique_word()}")

second_text = Text.from_file('the_stranger.txt')
print(f"You used word 'like' {second_text.get_word_frequency('like')} times")
print(f"Your most common word: {second_text.get_most_common_word()}")
# print(f"Unique words: {second_text.get_unique_word()}") # it's work, but better dont use (it's takes so much time)