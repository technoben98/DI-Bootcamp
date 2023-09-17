from game import Game

def get_user_menu_choice():
    user_choice = input("(g)Play a new game \n(x) Show scores and exit\n : ")
    return user_choice

def print_results(results):
    print(f"Game Results:\n You won {results['won']} times.\n You lose {results['lost']} times.\n You drew {results['draw']} times.\n\nThank you for playing!")

def main():
    results = {'won' : 0, 'lost' : 0, 'draw' : 0}
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == "g":
            new_game = Game()
            new_game = new_game.play()
            if new_game == 'win':
                new_result = results['won'] + 1
                results.update({'won' : new_result})
            elif new_game == 'lose':
                new_result = results['lost'] + 1
                results.update({'lost' : new_result})
            elif new_game == 'draw':
                new_result = results['draw'] + 1
                results.update({'draw' : new_result})
        elif user_choice == "x":
            print_results(results)
            break

main()