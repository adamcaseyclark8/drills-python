r"""TODO: port to Python.

Original JavaScript (test/hashing/contains-duplicates.test.js):

const arrayContainsDuplicates = require('../../code/hashing/contains-duplicates.js');

describe('array contains duplicates algorithm', () => {
    test('I: numbers', () => {
        const result = arrayContainsDuplicates([1, 2, 2, 3, 4, 4, 5]);
        expect(arrayContainsDuplicates([1, 2, 2, 3, 4, 4, 5])).toEqual(true);
    });

    test('II: strings', () => {
        expect(arrayContainsDuplicates(['a', 'b', 'a', 'c', 'b'])).toEqual(true);
    });

    test('III: false', () => {
        expect(arrayContainsDuplicates([10, 20, 30])).toEqual(false);
    });

    test('returns false array when input is empty', () => {
        expect(arrayContainsDuplicates([])).toEqual(false);
    });

    test('returns false array when only one element', () => {
        expect(arrayContainsDuplicates([1])).toEqual(false);
    });

    // my test cases above - chatgpt below
    test('returns false for empty array', () => {
        expect(arrayContainsDuplicates([])).toBe(false);
    });

    test('returns false when all elements are unique', () => {
        expect(arrayContainsDuplicates([1, 2, 3, 4])).toBe(false);
    });

    test('returns true when duplicates exist', () => {
        expect(arrayContainsDuplicates([1, 2, 3, 2])).toBe(true);
    });

    test('returns true when all elements are the same', () => {
        expect(arrayContainsDuplicates([5, 5, 5, 5])).toBe(true);
    });

    test('works with strings', () => {
        expect(arrayContainsDuplicates(['a', 'b', 'c', 'a'])).toBe(true);
        expect(arrayContainsDuplicates(['x', 'y', 'z'])).toBe(false);
    });

    // test('works with mixed types (number vs string)', () => {
    //     expect(arrayContainsDuplicates([1, '1'])).toBe(false); // different types
    // });
});

"""
