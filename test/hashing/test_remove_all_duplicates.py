r"""TODO: port to Python.

Original JavaScript (test/hashing/remove-all-duplicates.test.js):

const removeAllDuplicates = require('../../code/hashing/remove-all-duplicates.js');

describe('remove all duplicates algorithm', () => {
    test('removes duplicates from an array of numbers', () => {
        const result = removeAllDuplicates([1, 2, 2, 3, 4, 4, 5]);
        expect(result.sort()).toEqual([1, 2, 3, 4, 5]);
    });

    test('removes duplicates from an array of strings', () => {
        const result = removeAllDuplicates(['a', 'b', 'a', 'c', 'b']);
        expect(result.sort()).toEqual(['a', 'b', 'c']);
    });

    test('returns same array when no duplicates exist', () => {
        const result = removeAllDuplicates([10, 20, 30]);
        expect(result.sort()).toEqual([10, 20, 30]);
    });

    test('returns empty array when input is empty', () => {
        expect(removeAllDuplicates([])).toEqual([]);
    });

    test('works with all elements being the same', () => {
        const result = removeAllDuplicates([1, 1, 1, 1]);
        expect(result).toEqual([1]);
    });

    // test('handles mixed types (number and string)', () => {
    //     const result = removeAllDuplicates([1, '1', 2, '2', 1]);
    //     expect(result.length).toEqual(2);
    //     expect(result).toContain(1);
    //     expect(result).toContain(2);
    // });

    test('maintains order of first occurrence', () => {
        const result = removeAllDuplicates(['a', 'b', 'a', 'c']);
        expect(result).toEqual(['a', 'b', 'c']); // Set keeps first occurrence
    });

    // MY TEST CASES / ABOVE SUPPLIED BY CHATGPT
    test('multiple element array', () => {
        expect(removeAllDuplicates([1, 1, 2, 2, 3, 3, 3, 4])).toStrictEqual([1, 2, 3, 4]);
    });

    test('one element array', () => {
        expect(removeAllDuplicates([1])).toStrictEqual([1]);
    });
});

"""
