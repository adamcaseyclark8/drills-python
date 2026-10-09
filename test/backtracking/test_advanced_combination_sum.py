r"""TODO: port to Python.

Original JavaScript (test/backtracking/advanced-combination-sum.test.js):

const performAdvancedCombinationSum = require('../../code/backtracking/advanced-combination-sum');

// CANDIDATES MAY HAVE DUPLICATES
// EACH NUMBER USED ONCE ONLY
// NO DUPLICATE COMBINATIONS IN OUTPUT

describe('advanced combination sum', () => {
    test('basic case with duplicates in input', () => {
        const result = performAdvancedCombinationSum([10, 1, 2, 7, 6, 1, 5], 8);
        expect(result).toHaveLength(4);
        expect(result).toContainEqual([1, 1, 6]);
        expect(result).toContainEqual([1, 2, 5]);
        expect(result).toContainEqual([1, 7]);
        expect(result).toContainEqual([2, 6]);
    });

    test('no valid combination', () => {
        expect(performAdvancedCombinationSum([2, 4], 3)).toEqual([]);
    });

    test('no duplicate combinations in output', () => {
        const result = performAdvancedCombinationSum([1, 1, 1, 1], 2);
        expect(result).toHaveLength(1);
        expect(result).toContainEqual([1, 1]);
    });

    test('single element equals target', () => {
        const result = performAdvancedCombinationSum([1, 2, 3], 3);
        expect(result).toHaveLength(2);
        expect(result).toContainEqual([3]);
        expect(result).toContainEqual([1, 2]);
    });

    test('each element used at most once', () => {
        const result = performAdvancedCombinationSum([1, 2, 3], 4);
        expect(result).toHaveLength(1);
        expect(result).not.toContainEqual([2, 2]);
        expect(result).toContainEqual([1, 3]);
    });
});

"""
