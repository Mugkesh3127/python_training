def solve_sudoku(board):

    # Check if placing num at (row, col) is valid
    def is_valid(row, col, num):

        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    # Backtracking function
    def backtrack():

        for row in range(9):
            for col in range(9):

                # Find an empty cell
                if board[row][col] == ".":

                    # Try digits 1 to 9
                    for num in map(str, range(1, 10)):

                        if is_valid(row, col, num):
                            board[row][col] = num

                            if backtrack():
                                return True

                            # Undo choice (Backtrack)
                            board[row][col] = "."

                    # No valid number found
                    return False

        # Puzzle solved
        return True

    backtrack()


# -----------------------------
# Test
# -----------------------------
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)

print("Solved Sudoku:")
for row in board:
    print(" ".join(row))