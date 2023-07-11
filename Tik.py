import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + board[i][j] + " |", end="")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function for AI player's move
def ai_move(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                available_moves.append((i, j))
    move = random.choice(available_moves)
    board[move[0]][move[1]] = "O"

# Main game loop
def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = "X"
        print_board(board)
        if check_win(board, "X"):
            print("Congratulations! You won!")
            break

        # AI player's move
        ai_move(board)
        print_board(board)
        if check_win(board, "O"):
            print("AI player wins!")
            break

        # Check for a tie
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

# Start the game
play_game()
      
