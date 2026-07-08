def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        # Check boundaries and water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # Mark current land as visited
        grid[r][c] = '0'

        # Visit all 4 directions
        dfs(r + 1, c)   # Down
        dfs(r - 1, c)   # Up
        dfs(r, c + 1)   # Right
        dfs(r, c - 1)   # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


# Example
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print("Number of Islands:", num_islands(grid))