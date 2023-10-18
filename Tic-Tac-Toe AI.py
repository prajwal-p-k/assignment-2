import sys

# Define the board
board = [[' ' for x in range(3)] for y in range(3)]

# Check if the board is full
def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

# Check if there's a winner
def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # check columns
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # check diagonal
        return True

    return False

# Minimax algorithm for AI move
def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -10 + depth
    if check_win(board, 'O'):
        return 10 - depth
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Get best move for AI
def get_best_move(board):
    best_move = (-1, -1)
    best_value = -sys.maxsize
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_value:
                    best_move = (i, j)
                    best_value = move_val
    return best_move

# Display the board
def display_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
            if j < 2:
                print('|', end=' ')
        print()
        if i < 2:
            print('-'*5)

# Main game loop
def game():
    while True:
        display_board(board)
        x, y = map(int, input("Enter your move (row and column) separated by space: ").split())
        if board[x][y] == ' ':
            board[x][y] = 'X'
            if check_win(board, 'X'):
                display_board(board)
                print("You win!")
                break
            elif not is_full(board):
                i, j = get_best_move(board)
                board[i][j] = 'O'
                if check_win(board, 'O'):
                    display_board(board)
                    print("AI wins!")
                    break
            else:
                display_board(board)
                print("It's a tie!")
                break
        else:
            print("Invalid move. Try again.")

game()
