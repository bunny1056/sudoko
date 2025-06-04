def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            row += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j < 8:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0 and i < 8:
            print("- - - + - - - + - - -")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # row, col
    return None

def is_valid(board, num, row, col):
    # Check row
    if num in board[row]:
        return False
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check 3x3 box
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

# Sample 9x9 Sudoku board (0 represents empty cells)
sudoku_board = [
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

if solve_sudoku(sudoku_board):
    print("✅ Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("❌ No solution exists.")
