r"""TODO: port to Python.

Original JavaScript (test/hashing/top-k-frequent-elements.test.js):

const getTopKFrequentElements = require('../../code/hashing/top-k-frequent-elements.js');

describe('verify top k frequent elements', () => {
    test('returns top 2 frequent elements from a simple array', () => {
        expect(getTopKFrequentElements([1, 1, 1, 2, 2, 3], 2)).toStrictEqual(expect.arrayContaining([1, 2]));
    });

    test('returns the only element when k is 1', () => {
        expect(getTopKFrequentElements([4, 4, 4, 4], 1)).toStrictEqual([4]);
    });

    test('returns all unique elements when k equals number of unique elements', () => {
        expect(getTopKFrequentElements([1, 2, 3, 4], 4)).toStrictEqual(expect.arrayContaining([1, 2, 3, 4]));
    });

    test('returns element with highest frequency from array with mixed frequencies', () => {
        expect(getTopKFrequentElements([5, 3, 1, 1, 1, 3, 5, 5, 5], 1)).toStrictEqual([5]);
    });

    test('handles negative numbers and returns top k', () => {
        expect(getTopKFrequentElements([-1, -1, -2, -2, -2, 3], 2)).toStrictEqual(expect.arrayContaining([-1, -2]));
    });

    test('handles case where multiple elements have the same frequency', () => {
        const result = getTopKFrequentElements([1, 2, 3, 4], 2);
        expect([1, 2, 3, 4]).toEqual(expect.arrayContaining(result)); // any 2 out of 4
    });
});

"""
