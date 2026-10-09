r"""TODO: port to Python.

Original JavaScript (test/sliding-window/chunk-array-into-groups.test.js):

const chunkArrayIntoGroups = require('../../code/sliding-window/chunk-array-into-groups');

test('chunks evenly divisible array', () => {
    expect(chunkArrayIntoGroups([1, 2, 3, 4], 2)).toEqual([
        [1, 2],
        [3, 4]
    ]);
});

test('chunks with remainder', () => {
    expect(chunkArrayIntoGroups([1, 2, 3, 4, 5], 2)).toEqual([[1, 2], [3, 4], [5]]);
});

test('chunk size of 1', () => {
    expect(chunkArrayIntoGroups([1, 2, 3], 1)).toEqual([[1], [2], [3]]);
});

test('chunk size larger than array', () => {
    expect(chunkArrayIntoGroups([1, 2, 3], 5)).toEqual([[1, 2, 3]]);
});

test('empty array', () => {
    expect(chunkArrayIntoGroups([], 2)).toEqual([]);
});

test('chunk size equal to array length', () => {
    expect(chunkArrayIntoGroups([1, 2, 3], 3)).toEqual([[1, 2, 3]]);
});

"""
