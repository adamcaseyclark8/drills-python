r"""TODO: port to Python.

Original JavaScript (test/backtracking/perform-combination-sum.test.js):

const performCombinationSum = require('../../code/backtracking/perform-combination-sum.js');

describe('perform combination sum tests', () => {
    test('returns correct combinations for [2,3,6,7], target 7', () => {
        const result = performCombinationSum([2, 3, 6, 7], 7);
        expect(result).toEqual(expect.arrayContaining([[2, 2, 3], [7]]));
        expect(result).toHaveLength(2);
    });

    test('returns correct combinations for [2,3,5], target 8', () => {
        const result = performCombinationSum([2, 3, 5], 8);
        expect(result).toEqual(
            expect.arrayContaining([
                [2, 2, 2, 2],
                [2, 3, 3],
                [3, 5]
            ])
        );
        expect(result).toHaveLength(3);
    });

    test('returns empty when no combination exists', () => {
        expect(performCombinationSum([3, 5], 1)).toEqual([]);
    });

    test('single candidate that equals target', () => {
        expect(performCombinationSum([7], 7)).toEqual([[7]]);
    });

    test('candidate can be reused multiple times', () => {
        const result = performCombinationSum([2], 6);
        expect(result).toEqual([[2, 2, 2]]);
    });
});

"""
