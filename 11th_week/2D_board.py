def exist(board, word):
    if not board or not board[0]:
        return False

    rows = len(board)
    cols = len(board[0])

    def dfs(row, col, index):
        # Entire word matched
        if index == len(word):
            return True

        # Boundary and character check
        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False

        # Mark current cell as visited
        temp = board[row][col]
        board[row][col] = "#"

        # Explore all 4 directions
        found = (
            dfs(row + 1, col, index + 1) or
            dfs(row - 1, col, index + 1) or
            dfs(row, col + 1, index + 1) or
            dfs(row, col - 1, index + 1)
        )

        # Restore original value (Backtrack)
        board[row][col] = temp

        return found

    # Try starting from every cell
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


# -----------------------------
# Test
# -----------------------------
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCCED"

print(exist(board, word))