import random

class Game:

    def get_user_item(self):
        while True:
            user_item = input("Select: (r)ock, (p)aper, (s)cissors: ")
            if user_item == "r" or user_item == "p" or user_item == "s":
                return user_item
        
    def get_computer_item(self):
        rps_list = ["r", "s", "p"]
        return random.choice(rps_list)
        
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == "r" and computer_item == "s" or \
        user_item == "s" and computer_item == "p" or \
        user_item == "p" and computer_item == "r":
            return "win"
        else:
            return "lose"
        
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        if result == "win":
            print(f"You selected {user_item}. The computer selected {computer_item}. You {result}!")
            return "win"
        elif result == "lose":
            print(f"You selected {user_item}. The computer selected {computer_item}. You {result}!")
            return "lose"
        elif result == "draw":
            print(f"You selected {user_item}. The computer selected {computer_item}. You {result}!")
            return "draw"