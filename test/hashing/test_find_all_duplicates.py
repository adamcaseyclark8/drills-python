r"""TODO: port to Python.

Original JavaScript (test/hashing/find-all-duplicates.test.js):

const findAllDuplicates = require('../../code/hashing/find-all-duplicates');

// RETURNS NUMBER DUPLICATED (NOT THE INDEX OF DUPLICATES)
// RETURNS EMPTY ARRAY IF NO DUPLICATES

describe('find all duplicates test', () => {
    test('returns duplicates from standard case', () => {
        expect(findAllDuplicates([4, 3, 2, 7, 8, 2, 3, 1])).toEqual([2, 3]);
    });

    test('returns empty array when no duplicates', () => {
        expect(findAllDuplicates([1, 2, 3, 4])).toEqual([]);
    });

    test('returns all elements when all are duplicates', () => {
        expect(findAllDuplicates([1, 1, 2, 2, 3, 3])).toEqual([1, 2, 3]);
    });

    test('returns single duplicate', () => {
        expect(findAllDuplicates([1, 2, 3, 2])).toEqual([2]);
    });

    test('returns empty array for single element', () => {
        expect(findAllDuplicates([5])).toEqual([]);
    });

    test('returns empty array for empty input', () => {
        expect(findAllDuplicates([])).toEqual([]);
    });

    test('handles duplicate at start of array', () => {
        expect(findAllDuplicates([3, 3, 1, 2])).toEqual([3]);
    });
});

"""
