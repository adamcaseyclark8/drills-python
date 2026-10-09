r"""TODO: port to Python.

Original JavaScript (test/hashing/get-all-sum-to-zero.test.js):

const getAllPairsThatSumToZero = require('../../code/hashing/get-all-sum-to-zero.js');

describe('get all pairs that sum to zero', () => {
    test('returns pairs that sum to zero', () => {
        expect(getAllPairsThatSumToZero([-3, -1, 0, 1, 2, 3])).toEqual([
            [-1, 1],
            [-3, 3]
        ]);
    });

    test('returns empty array when no pairs sum to zero', () => {
        expect(getAllPairsThatSumToZero([1, 2, 3])).toEqual([]);
    });

    test('returns empty array for empty input', () => {
        expect(getAllPairsThatSumToZero([])).toEqual([]);
    });

    test('handles multiple pairs', () => {
        expect(getAllPairsThatSumToZero([-2, -1, 1, 2])).toEqual([
            [-1, 1],
            [-2, 2]
        ]);
    });

    test('returns empty when no negatives present', () => {
        expect(getAllPairsThatSumToZero([1, 2, 3, 4])).toEqual([]);
    });
});

"""
