r"""TODO: port to Python.

Original JavaScript (test/math/find-duplicate-number.test.js):

const findDuplicateNumber = require('../../code/math/find-duplicate-number.js');

describe('find duplicate number algo', () => {
    test('finds a simple duplicate', () => {
        expect(findDuplicateNumber([1, 3, 4, 2, 2])).toStrictEqual([2]);
    });

    // test('finds duplicate appearing multiple times', () => {
    //     expect(findDuplicateNumber([3, 1, 3, 4, 2, 3])).toStrictEqual([3]);
    // });

    test('finds duplicate at beginning and end', () => {
        expect(findDuplicateNumber([5, 4, 3, 2, 1, 5])).toStrictEqual([5]);
    });

    test('returns -1 if no duplicate (edge case)', () => {
        expect(findDuplicateNumber([1, 2, 3, 4])).toStrictEqual(-1);
    });

    test('works with smallest valid array', () => {
        expect(findDuplicateNumber([1, 1])).toStrictEqual([1]);
    });

    test('works when duplicate is the largest number', () => {
        expect(findDuplicateNumber([1, 2, 3, 4, 5, 5])).toStrictEqual([5]);
    });

    test('works when duplicate is the smallest number', () => {
        expect(findDuplicateNumber([1, 1, 2, 3, 4, 5])).toStrictEqual([1]);
    });

    test('handles unordered input', () => {
        expect(findDuplicateNumber([9, 8, 7, 6, 9, 5, 4, 3, 2, 1])).toStrictEqual([9]);
    });
});

"""
