r"""TODO: port to Python.

Original JavaScript (test/hashing/two-number-sum-set.test.js):

const twoNumberSumUsingSet = require('../../code/hashing/two-number-sum-set.js');

// RETURN NUMBERS (NOT INDICES)
// RETURNS ALL PAIRS OF MATCHES
// USES A SET DATA STRUCTURE

describe('perform two number sum using set', () => {
    test('returns pair of numbers that sum to target (simple case)', () => {
        const result = twoNumberSumUsingSet([3, 5, -4, 8, 11, 1, -1, 6], 10);
        expect(result.length).toEqual(1);
        expect(result[0]).toEqual([11, -1]);
    });

    test('returns pair when numbers are at the start/end of the array', () => {
        const result = twoNumberSumUsingSet([1, 2, 3, 8, 5], 6);
        expect(result.length).toEqual(1);
        expect(result[0]).toEqual([1, 5]);
    });

    test('returns empty array when no two numbers sum to target', () => {
        const result = twoNumberSumUsingSet([1, 2, 3, 4], 100);
        expect(result).toEqual([]);
    });

    test('handles negative numbers correctly', () => {
        const result = twoNumberSumUsingSet([-3, -1, -5, -4], -5);
        expect(result.length).toEqual(1);
        expect(result[0]).toEqual([-1, -4]);
    });

    test('returns first valid pair it finds (when multiple are possible)', () => {
        const result = twoNumberSumUsingSet([2, 4, 6, 8], 10);
        expect(result.length).toEqual(2);
        expect(result.sort()).toEqual(
            [
                [4, 6],
                [2, 8]
            ].sort()
        );
    });

    test('returns empty array when input array is empty', () => {
        const result = twoNumberSumUsingSet([], 10);
        expect(result).toEqual([]);
    });

    test('returns empty array when array has only one element', () => {
        const result = twoNumberSumUsingSet([10], 10);
        expect(result).toEqual([]);
    });

    test('returns correct result with duplicate numbers', () => {
        const result = twoNumberSumUsingSet([5, 5, 3], 10);
        expect(result.length).toEqual(1);
        expect(result[0]).toEqual([5, 5]);
    });

    test('does not use the same element twice', () => {
        const result = twoNumberSumUsingSet([5], 10);
        expect(result).toEqual([]);
    });

    test('3 matches', () => {
        const result = twoNumberSumUsingSet([1, 2, 3, 4, 5, 6, 7], 8);
        expect(result.length).toEqual(3);
        expect(result.sort()).toEqual(
            [
                [1, 7],
                [2, 6],
                [3, 5]
            ].sort()
        );
    });
});

"""
