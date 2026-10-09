from collections import deque


def count_number_of_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        [1, 0],  # down
        [-1, 0],  # up
        [0, 1],  # right
        [0, -1],  # left
    ]

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # mark as visited

        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in directions:
                new_r = cur_r + dr
                new_c = cur_c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1':
                    queue.append((new_r, new_c))
                    grid[new_r][new_c] = '0'  # mark as visited

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)

    return count
