r"""TODO: port to Python.

Original JavaScript (test/arrays/rotate-array-in-place.test.js):

const rotateArrayInPlace = require('../../code/arrays/rotate-array-in-place');

// MOVE START OF INDEX BACKWARDS IN ARRAY
// CHANGE IS 3 => START GOES FROM INDEX 0 TO INDEX 3
//
// RULES:
// 1.) CHANGE HAS TO BE NUMBER
// 2.) CHANGE HAS TO BE GREATER THAN ZERO
// 3.) MUST HANDLE NULL AND EMPTY ARRAY

describe('rotateArrayInPlace', () => {
    test('basic case - k=3', () => {
        expect(rotateArrayInPlace([1, 2, 3, 4, 5, 6, 7], 3)).toEqual([5, 6, 7, 1, 2, 3, 4]);
    });

    test('k=1 shifts everything one step right', () => {
        expect(rotateArrayInPlace([1, 2, 3], 1)).toEqual([3, 1, 2]);
    });

    test('k equals array length - back to original', () => {
        expect(rotateArrayInPlace([1, 2, 3, 4], 4)).toEqual([1, 2, 3, 4]);
    });

    test('k larger than array length - wraps around', () => {
        expect(rotateArrayInPlace([1, 2, 3, 4, 5, 6, 7], 10)).toEqual([5, 6, 7, 1, 2, 3, 4]);
    });

    test('k=0 - no change', () => {
        expect(rotateArrayInPlace([1, 2, 3], 0)).toEqual([1, 2, 3]);
    });

    test('single element array', () => {
        expect(rotateArrayInPlace([1], 5)).toEqual([1]);
    });

    test('two element array', () => {
        expect(rotateArrayInPlace([1, 2], 1)).toEqual([2, 1]);
    });

    test('all same values', () => {
        expect(rotateArrayInPlace([3, 3, 3, 3], 2)).toEqual([3, 3, 3, 3]);
    });
});

"""
