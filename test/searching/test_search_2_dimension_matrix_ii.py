r"""TODO: port to Python.

Original JavaScript (test/searching/search-2-dimension-matrix-ii.test.js):

const search2DMatrix = require('../../code/searching/search-2-dimension-matrix-ii.js');

describe('search a 2 d matrix', () => {
    test('returns true when target exists in matrix', () => {
        const matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ];
        expect(search2DMatrix(matrix, 3)).toBe(true);
        expect(search2DMatrix(matrix, 16)).toBe(true);
        expect(search2DMatrix(matrix, 50)).toBe(true);
    });

    test('returns false when target does not exist', () => {
        const matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ];
        expect(search2DMatrix(matrix, 13)).toBe(false);
        expect(search2DMatrix(matrix, 0)).toBe(false);
        expect(search2DMatrix(matrix, 51)).toBe(false);
    });

    test('handles empty matrix', () => {
        expect(search2DMatrix([], 1)).toBe(false);
        expect(search2DMatrix([[]], 1)).toBe(false);
    });

    test('handles single-row matrix', () => {
        const matrix = [[1, 2, 3, 4, 5]];
        expect(search2DMatrix(matrix, 3)).toBe(true);
        expect(search2DMatrix(matrix, 6)).toBe(false);
    });

    test('handles single-column matrix', () => {
        const matrix = [[1], [3], [5], [7]];
        expect(search2DMatrix(matrix, 5)).toBe(true);
        expect(search2DMatrix(matrix, 2)).toBe(false);
    });

    test('handles 1x1 matrix', () => {
        expect(search2DMatrix([[1]], 1)).toBe(true);
        expect(search2DMatrix([[1]], 2)).toBe(false);
    });

    test('handles negative numbers', () => {
        const matrix = [
            [-10, -5, -1],
            [0, 3, 7],
            [10, 12, 15]
        ];
        expect(search2DMatrix(matrix, -5)).toBe(true);
        expect(search2DMatrix(matrix, 12)).toBe(true);
        expect(search2DMatrix(matrix, -6)).toBe(false);
    });
});

"""
