r"""TODO: port to Python.

Original JavaScript (test/two-pointers/change-starting-index.test.js):

const changeStartingIndex = require('../../code/two-pointers/change-starting-index.js');

// MOVE START OF INDEX FORWARDS IN ARRAY
// CHANGE IS 3 => START GOES FROM INDEX 0 TO INDEX ARRAY.LENGTH - 3
//
// RULES:
// 1.) CHANGE HAS TO BE NUMBER
// 2.) CHANGE HAS TO BE GREATER THAN ZERO
// 3.) MUST HANDLE NULL AND EMPTY ARRAY

describe('verify change starting index function', () => {
    test('given test case', () => {
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 2)).toStrictEqual([3, 4, 5, 6, 7, 1, 2]);
    });

    test('another test case', () => {
        expect(changeStartingIndex([7, 1, 2, 3, 4, 5, 6], 6)).toStrictEqual([6, 7, 1, 2, 3, 4, 5]);
    });

    test('when array is unordered', () => {
        expect(changeStartingIndex([3, 4, 5, 6, 7, 1, 2], 2)).toStrictEqual([5, 6, 7, 1, 2, 3, 4]);
    });

    test('with small array', () => {
        expect(changeStartingIndex([1, 2], 1)).toStrictEqual([2, 1]);
    });

    test('when starting index loops array many times', () => {
        expect(changeStartingIndex([1, 2], 8)).toStrictEqual([1, 2]);
    });

    test('when the starting index is zero', () => {
        expect(changeStartingIndex([1, 2], 0)).toStrictEqual([1, 2]);
    });

    test('when the array is empty', () => {
        expect(changeStartingIndex([], 3)).toStrictEqual([]);
    });

    test('should throw an error when negative integer used', () => {
        expect(() => changeStartingIndex([1, 2, 3, 4, 5, 6, 7], -1)).toThrow('change must be an positive integer');
    });

    test('every iteration', () => {
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 1)).toStrictEqual([2, 3, 4, 5, 6, 7, 1]);
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 2)).toStrictEqual([3, 4, 5, 6, 7, 1, 2]);
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 3)).toStrictEqual([4, 5, 6, 7, 1, 2, 3]);
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 4)).toStrictEqual([5, 6, 7, 1, 2, 3, 4]);
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 5)).toStrictEqual([6, 7, 1, 2, 3, 4, 5]);
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 6)).toStrictEqual([7, 1, 2, 3, 4, 5, 6]);
        expect(changeStartingIndex([1, 2, 3, 4, 5, 6, 7], 7)).toStrictEqual([1, 2, 3, 4, 5, 6, 7]);
    });
});

"""
