r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/searching/02-find-three-largest/test/index.test.js):

const { findThreeLargestNumbers } = require('../code/index-by-algo');
// const {} = require('../code/index')

describe('', () => {
    test('test case #1', () => {
        const array = [55, 7, 8];
        expect(findThreeLargestNumbers(array)).toStrictEqual([7, 8, 55]);
    });

    test('test case #2', () => {
        const array = [55, 43, 11, 3, -3, 10];
        expect(findThreeLargestNumbers(array)).toStrictEqual([11, 43, 55]);
    });

    test('test case #3', () => {
        const array = [7, 8, 3, 11, 43, 55];
        expect(findThreeLargestNumbers(array)).toStrictEqual([11, 43, 55]);
    });

    test('test case #4', () => {
        const array = [55, 7, 8, 3, 43, 11];
        expect(findThreeLargestNumbers(array)).toStrictEqual([11, 43, 55]);
    });

    test('test case #5', () => {
        const array = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7];
        expect(findThreeLargestNumbers(array)).toStrictEqual([7, 7, 7]);
    });

    test('test case #6', () => {
        const array = [7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7];
        expect(findThreeLargestNumbers(array)).toStrictEqual([7, 7, 8]);
    });

    test('test case #7', () => {
        const array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7];
        expect(findThreeLargestNumbers(array)).toStrictEqual([18, 141, 541]);
    });

    test('test case #8', () => {
        const array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7];
        expect(findThreeLargestNumbers(array)).toStrictEqual([-2, -1, 7]);
    });
});

"""
