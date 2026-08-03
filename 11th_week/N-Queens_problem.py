def solve_n_queens(n):
    result = []
    board = [["." for _ in range(n)] for _ in range(n)]

    def is_safe(row, col):
        # Check same column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"

                backtrack(row + 1)

                board[row][col] = "."

    backtrack(0)
    return result


# -----------------------------
# Test
# -----------------------------
solutions = solve_n_queens(4)

print("Number of Solutions:", len(solutions))

for i, solution in enumerate(solutions, 1):
    print(f"\nSolution {i}")
    for row in solution:
        print(row)