r"""TODO: port to Python.

Original JavaScript (code/graphs/count-number-of-islands/code/index/bfs.js):

const countNumberOfIslands = grid => {
    if (!grid || grid.length === 0) return 0;

    const rows = grid.length;
    const cols = grid[0].length;
    let count = 0;

    const directions = [
        [1, 0], // down
        [-1, 0], // up
        [0, 1], // right
        [0, -1] // left
    ];

    function bfs(r, c) {
        const queue = [[r, c]];
        grid[r][c] = '0'; // mark as visited

        while (queue.length > 0) {
            const [curR, curC] = queue.shift();
            for (const [dr, dc] of directions) {
                const newR = curR + dr;
                const newC = curC + dc;

                if (newR >= 0 && newR < rows && newC >= 0 && newC < cols && grid[newR][newC] === '1') {
                    queue.push([newR, newC]);
                    grid[newR][newC] = '0'; // mark as visited
                }
            }
        }
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1') {
                count++;
                bfs(r, c);
            }
        }
    }

    return count;
};

module.exports = countNumberOfIslands;

"""
