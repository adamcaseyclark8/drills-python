r"""TODO: port to Python.

Original JavaScript (code/graphs/count-number-of-islands.js):

const countNumberOfIslands = grid => {
    if (!grid || grid.length === 0) return 0;

    const rows = grid.length;
    const columns = grid[0].length;
    let count = 0;

    const dfs = (r, c) => {
        // Base cases: Out of bounds or water
        if (r < 0 || c < 0 || r >= rows || c >= columns || grid[r][c] === '0') {
            return;
        }

        // Mark the land as visited
        grid[r][c] = '0';

        // Visit all 4 adjacent directions
        dfs(r + 1, c); // down
        dfs(r - 1, c); // up
        dfs(r, c + 1); // right
        dfs(r, c - 1); // left
    };

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < columns; c++) {
            if (grid[r][c] === '1') {
                count++;
                dfs(r, c);
            }
        }
    }

    return count;
};

module.exports = countNumberOfIslands;

"""
