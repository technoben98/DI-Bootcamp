import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
user_letter = ""
user_word = []
used_letters = []
turns = 0
win_or_lose = True
def play(word):
    while len(user_word) < len(word):
            user_word.append("*")
    if " " in word:
        space_index = word.index(" ")
        user_word.insert(space_index, " ")
        user_word.pop()
    check_letter(word, user_word)

def check_letter(word, user_word):
    while check_win() == True:
        print(user_word)
        user_letter = input("Type your letter:\n")
        if user_letter not in used_letters:
            if user_letter in word:
                for index, letter in enumerate(word):
                    if user_letter == letter:
                        user_word[index] = user_letter
                used_letters.append(user_letter)
            elif user_letter not in word:
                print(f"It's not letter {user_letter} in this word.")
                used_letters.append(user_letter)
                global turns
                turns = turns + 1
                draw_hangman()
        else:
            print("You already have this letter!")
    

def check_win():
    if "*" not in user_word:
        print("You won!")
        return False
    elif turns == 6:
        print ("You lose!")
        return False
    else:
        return True

def draw_hangman ():
        
    if turns >= 1:
        print("  |  ")
        print("  O  ")
    if turns == 2:
        print("  |  ")
    if turns == 3:
        print(" /|  ")
    if turns >= 4:
        print(" /|\ ")
    if turns == 5:
        print(" /   ")
    if turns == 6:
        print(" / \ ")
play(word)