def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    row = 0
    col = cols - 1

    while row < rows and col >= 0:

        if matrix[row][col] == target:
            return True

        elif matrix[row][col] > target:
            # Move left
            col -= 1

        else:
            # Move down
            row += 1

    return False


# -----------------------------
# Test
# -----------------------------
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

target = 5

if search_matrix(matrix, target):
    print(f"{target} found in matrix")
else:
    print(f"{target} not found in matrix")