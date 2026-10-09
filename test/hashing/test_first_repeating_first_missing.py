r"""TODO: port to Python.

Original JavaScript (test/hashing/first-repeating-first-missing.test.js):

const firstRepeatingFirstMissing = require('../../code/hashing/first-repeating-first-missing.js');

// HANDLES ARRAY WITH ONE ELEMENT
// HANDLES NO REPEATING ELEMENT
// HANDLES NO MISSING ELEMENT

describe('first repeating and first missing algo', () => {
    test('finds first missing and repeating in a simple case', () => {
        expect(firstRepeatingFirstMissing([1, 3, 4, 5, 3])).toEqual([3, 2]);
    });

    test('handles array with repeating first element', () => {
        expect(firstRepeatingFirstMissing([2, 2, 3, 4, 5])).toEqual([2, 1]);
    });

    test('handles missing 1', () => {
        expect(firstRepeatingFirstMissing([2, 3, 4, 4, 5])).toEqual([4, 1]);
    });

    test('handles duplicate in middle', () => {
        expect(firstRepeatingFirstMissing([1, 2, 2, 3, 5])).toEqual([2, 4]);
    });

    test('works when last element repeats', () => {
        expect(firstRepeatingFirstMissing([1, 2, 3, 5, 5])).toEqual([5, 4]);
    });

    test('works with negatives and zeros', () => {
        expect(firstRepeatingFirstMissing([0, -1, 1, 3, 3, 5])).toEqual([3, 2]);
    });

    test('handles array with only one element', () => {
        expect(firstRepeatingFirstMissing([1])).toEqual([-1, 2]);
    });

    test('handles no repeating element', () => {
        expect(firstRepeatingFirstMissing([1, 2, 3, 4, 5])).toEqual([-1, 6]);
    });

    test('handles no missing element but has repeat', () => {
        expect(firstRepeatingFirstMissing([1, 2, 3, 4, 4, 5])).toEqual([4, 6]);
    });

    test('works with unordered input', () => {
        expect(firstRepeatingFirstMissing([3, 1, 4, 2, 2])).toEqual([2, 5]);
    });
});

"""
