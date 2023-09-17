class AnagramChecker:
    def __init__(self, file):
        with open(file, 'r') as file:
            self.word_list = file.read().splitlines()

    def is_valid_word(self, word):
        return word.lower() in self.word_list
    
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w):
                if word != w:
                    anagrams.append(w)
        return anagrams