import sys

def find_possible_values(board, row, col):
    possible_values = set(range(1, 10))
    
    # Check row
    possible_values -= set(board[row])
    
    # Check column
    possible_values -= set(board[i][col] for i in range(9))
    
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            possible_values.discard(board[i][j])
    
    return possible_values

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    possible_values = find_possible_values(board, row, col)
    for num in possible_values:
        board[row][col] = num
        if solve_sudoku(board):
            return True
        board[row][col] = 0
    
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

board = []
for i in range(9):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(tmp)
    
solve_sudoku(board)
for row in board:
    print(*row)