r"""TODO: port to Python.

Original JavaScript (code/matrices/rotate-matrix.js):

const rotate = matrix => {
    const n = matrix.length;

    // Step 1: Transpose the matrix (swap rows and columns)
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }

    // Step 2: Reverse each row
    for (let row of matrix) {
        row.reverse();
    }

    return matrix;
};

module.exports = rotate;

// [1, 2],
// [3, 4]

// [3, 1],
// [4, 2]

"""
