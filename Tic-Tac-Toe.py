def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    for _ in range(9): # maximum 9 moves in tic-tac-toe
        print_board(board)
        print(f"It's {current_player}'s turn.")
        row, col = -1, -1
        while row not in [0, 1, 2] or col not in [0, 1, 2] or board[row][col] != ' ':
            try:
                row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
            except ValueError:
                pass

        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} Wins!")
            return
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    print("It's a Tie!")

if __name__ == '__main__':
    main()
