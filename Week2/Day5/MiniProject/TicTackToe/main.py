board = list(range(1,10))
def display_board(board):
    print(" TIC-TAC-TOE")
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

def player_input (player):
    while True:
        player_answer = int(input(f"{player}, your turn to choose cell:\n"))
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player
                return False
            else:
                print("Choose other cell!")
        
def check_win(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
    return False

def play (board):
    counter = 0
    win = False
    while not win:
        display_board(board)
        if counter % 2 == 0:
           player_input("X")
        else:
           player_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "you won!")
              win = True
              break
        if counter == 9:
            print("Nobody wins")
            break
    display_board(board)
play(board)