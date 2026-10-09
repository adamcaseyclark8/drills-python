r"""TODO: port to Python.

Original JavaScript (test/hashing/two-number-sum-map.test.js):

const twoNumberSumUsingMap = require('../../code/hashing/two-number-sum-map.js');

// RETURN INDICES OF NUMBERS (NOT NUMBERS)
// ONLY RETURNS FIRST PAIR OF MATCHES
// USES A HASHMAP DATA STRUCTURE

describe('perform two number sum using map', () => {
    test('returns indices of two numbers that add to target', () => {
        expect(twoNumberSumUsingMap([2, 7, 11, 15], 9)).toEqual([0, 1]);
    });

    test('target pair is not at the start', () => {
        expect(twoNumberSumUsingMap([3, 2, 4], 6)).toEqual([1, 2]);
    });

    test('duplicate values', () => {
        expect(twoNumberSumUsingMap([3, 3], 6)).toEqual([0, 1]);
    });

    test('negative numbers', () => {
        expect(twoNumberSumUsingMap([-3, 4, 3, 90], 0)).toEqual([0, 2]);
    });

    test('negative target', () => {
        expect(twoNumberSumUsingMap([-1, -2, -3, -4], -6)).toEqual([1, 3]);
    });

    test('larger array, pair near the end', () => {
        expect(twoNumberSumUsingMap([1, 5, 3, 8, 2, 7], 9)).toEqual([0, 3]);
    });

    test('zero as one of the values', () => {
        expect(twoNumberSumUsingMap([0, 4, 3, 0], 0)).toEqual([0, 3]);
    });
});

"""
