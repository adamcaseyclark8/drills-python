class UnionFind:
    def __init__(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        self.count = 0
        self.parent = list(range(rows * cols))
        self.rank = [0] * (rows * cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # path compression
        return self.parent[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1

    def get_count(self):
        return self.count


def num_islands_union_find(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    uf = UnionFind(grid)

    directions = [[1, 0], [0, 1]]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        id1 = r * cols + c
                        id2 = nr * cols + nc
                        uf.union(id1, id2)

    return uf.get_count()
