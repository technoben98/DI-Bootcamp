import anagram_cheker

def main():
    word_list_file = 'angrams_sowpods.txt'
    checker = anagram_cheker.AnagramChecker(word_list_file)

    while True:
        choice = input("Enter your choice: \n1. Input a word \n2. Exit\n")

        if choice == "1":
            word = input("Enter a word: ").upper()
            word = word.strip()
            
            if len(word.split()) > 1:
                print("Error: Only a single word is allowed.")
                continue
            
            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue
            
            anagrams = checker.get_anagrams(word)
            num_anagrams = len(anagrams)
            
            if num_anagrams == 0:
                print(f"There are no anagrams for '{word}'.")
            else:
                print(f"Your word: {word.upper()}")
                anagrams_string = ""
                for anagram in anagrams:
                    if anagrams.index(anagram) < len(anagrams)-1:
                        anagrams_string = anagrams_string + anagram + ", "
                    else:
                        anagrams_string = anagrams_string + anagram + "."
                print(f"Anagrams for your word: {anagrams_string}")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

main()