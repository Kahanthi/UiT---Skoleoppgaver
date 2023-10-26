
def illegal_move(player):
    print(f"Player {player}, the square you picked is already filled. Pick another one.")

def get_player_symbols():
    symbol_1 = input("Player 1, do you want to be X or O? ").upper()
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are O.")
    elif symbol_1 == "O":
        symbol_2 = "X"
        print("Player 2, you are X.")
    else:
        print("Invalid choice. Defaulting to X for Player 2.")
        symbol_1 = "X"
        symbol_2 = "O"

    input("Press enter to continue.\n")
    return symbol_1, symbol_2

def create_empty_grid():
    print("Here is the playboard:")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    print_board(board)
    return board

def play_turn(board, symbol_1, symbol_2, player):
    print(f"{player}, it is your turn.")
    row = int(input("Pick a row [1, 2, 3]: ")) - 1  
    column = int(input("Pick a column [1, 2, 3]: ")) - 1  

    while not (0 <= row < 3) or not (0 <= column < 3):
        print("Out of board. Pick another one.")
        row = int(input("Pick a row [1, 2, 3]: ")) - 1  
        column = int(input("Pick a column [1, 2, 3]: ")) - 1  

    while board[row][column] == symbol_1 or board[row][column] == symbol_2:
        illegal_move(player)
        row = int(input("Pick a row [1, 2, 3]: ")) - 1 
        column = int(input("Pick a column [1, 2, 3]: ")) - 1 

    board[row][column] = symbol_1 if player == "Player 1" else symbol_2
    print_board(board)

def print_board(board):
    print("Here is the updated playboard:")
    for row in board:
        print("---+---+---")
        print(row[0], " |", row[1], "|", row[2])
    print("---+---+---")

def check_win(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

def main():
    print("Hello! Welcome to isak's Tic Tac Toe game!\n")
    board = create_empty_grid()
    symbol_1, symbol_2 = get_player_symbols()
    count = 0

    while count < 9:
        player = "Player 1" if count % 2 == 0 else "Player 2"
        play_turn(board, symbol_1, symbol_2, player)

        if check_win(board, symbol_1):
            print("Player 1 wins! Congratulations!")
            break
        elif check_win(board, symbol_2):
            print("Player 2 wins! Congratulations!")
            break

        count += 1

    if count == 9:
        print("The board is full. Game over.")
        print("It's a tie.")
        
if __name__ == "__main__":
    main()