def count_number_of_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    count = 0

    def dfs(r, c):
        # Base cases: Out of bounds or water
        if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == '0':
            return

        # Mark the land as visited
        grid[r][c] = '0'

        # Visit all 4 adjacent directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count
