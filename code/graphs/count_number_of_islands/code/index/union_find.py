r"""TODO: port to Python.

Original JavaScript (code/graphs/count-number-of-islands/code/index/union-find.js):

class UnionFind {
    constructor(grid) {
        const rows = grid.length;
        const cols = grid[0].length;
        this.count = 0;
        this.parent = Array(rows * cols)
            .fill(0)
            .map((_, i) => i);
        this.rank = Array(rows * cols).fill(0);

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (grid[r][c] === '1') {
                    this.count++;
                }
            }
        }
    }

    find(i) {
        if (this.parent[i] !== i) {
            this.parent[i] = this.find(this.parent[i]); // path compression
        }
        return this.parent[i];
    }

    union(x, y) {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX === rootY) return;

        // union by rank
        if (this.rank[rootX] < this.rank[rootY]) {
            this.parent[rootX] = rootY;
        } else if (this.rank[rootX] > this.rank[rootY]) {
            this.parent[rootY] = rootX;
        } else {
            this.parent[rootY] = rootX;
            this.rank[rootX]++;
        }

        this.count--;
    }

    getCount() {
        return this.count;
    }
}

function numIslandsUnionFind(grid) {
    if (!grid || grid.length === 0) return 0;

    const rows = grid.length;
    const cols = grid[0].length;
    const uf = new UnionFind(grid);

    const directions = [
        [1, 0],
        [0, 1]
    ];

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1') {
                grid[r][c] = '0';
                for (const [dr, dc] of directions) {
                    const nr = r + dr;
                    const nc = c + dc;
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] === '1') {
                        const id1 = r * cols + c;
                        const id2 = nr * cols + nc;
                        uf.union(id1, id2);
                    }
                }
            }
        }
    }

    return uf.getCount();
}

module.exports = numIslandsUnionFind;

"""
