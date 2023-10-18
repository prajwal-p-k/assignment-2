def is_valid(board, row, col, num):
    """Check if it's valid to place `num` at `board[row][col]`."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solve_sudoku(board):
    """Solve the Sudoku board using backtracking."""
    empty = find_empty_cell(board)
    if not empty:
        return True
    row, col = empty

    for i in range(1, 10):
        if is_valid(board, row, col, i):
            board[row][col] = i
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False

def find_empty_cell(board):
    """Find an empty cell in the Sudoku board. Return (row, col) or None if full."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

if __name__ == "__main__":
    sample_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sample_board):
        for row in sample_board:
            print(row)
    else:
        print("No solution found!")
