r"""TODO: port to Python.

Original JavaScript (test/searching/binary-search.test.js):

const performBinarySearch = require('../../code/searching/binary-search.js');

describe('test binary search', () => {
    test('test case #1', () => {
        expect(performBinarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)).toBe(3);
    });

    test('test case #2', () => {
        const array = [1, 5, 23, 111];
        expect(performBinarySearch(array, 5)).toBe(1);
    });

    test('test case #3', () => {
        const array = [1, 5, 23, 111];
        expect(performBinarySearch(array, 35)).toBe(-1);
    });

    test('test case #1', () => {
        const array = [1, 5, 23, 111];
        expect(performBinarySearch(array, 111)).toBe(3);
    });

    test('test case #5', () => {
        const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73];
        expect(performBinarySearch(array, 72)).toBe(8);
    });

    test('test case #6', () => {
        const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73];
        expect(performBinarySearch(array, 73)).toBe(9);
    });

    test('test case #7', () => {
        const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73];
        expect(performBinarySearch(array, 70)).toBe(-1);
    });

    test('test case #8', () => {
        const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355];
        expect(performBinarySearch(array, 355)).toBe(10);
    });

    test('test case #9', () => {
        const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 354];
        expect(performBinarySearch(array, 355)).toBe(-1);
    });
});

"""
