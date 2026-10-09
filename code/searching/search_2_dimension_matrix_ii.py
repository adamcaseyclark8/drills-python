r"""TODO: port to Python.

Original JavaScript (code/searching/search-2-dimension-matrix-ii.js):

// integers in each row are sorted in ascending order.
// the first integer of each row is greater than the last integer of the previous row.

const search2DMatrix = (matrix, target) => {
    if (!matrix.length || !matrix[0].length) return false;

    const m = matrix.length;
    const n = matrix[0].length;

    let left = 0;
    let right = m * n - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const midValue = matrix[Math.floor(mid / n)][mid % n];

        if (midValue === target) return true;
        if (midValue < target) left = mid + 1;
        else right = mid - 1;
    }

    return false;
};

module.exports = search2DMatrix;

"""
