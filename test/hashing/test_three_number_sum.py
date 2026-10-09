r"""TODO: port to Python.

Original JavaScript (test/hashing/three-number-sum.test.js):

const threeNumberSum = require('../../code/hashing/three-number-sum');

describe('three number sum', () => {
    test('An Array With Less Than 3 Numbers Returns False', () => {
        expect(threeNumberSum([3, 6], 9)).toEqual(false);
    });

    test("3 Numbers That Does Add Up Doesn't Work", () => {
        expect(threeNumberSum([1, 2, 3], 7)).toEqual(false);
    });

    test('4 Numbers That Sums To Target Returns False', () => {
        expect(threeNumberSum([1, 2, 3, 4], 10)).toEqual(false);
    });

    test('Three Numbers Works', () => {
        expect(threeNumberSum([3, 5, 1], 9)).toEqual(true);
    });

    test('Array Can Be Include Zero', () => {
        expect(threeNumberSum([3, 6, 0], 9)).toEqual(true);
    });

    test('Duplicated Numbers In The Array Works', () => {
        expect(threeNumberSum([3, 6, 0, 3], 9)).toEqual(true);
    });

    test("Negative Numbers After Passing Works - Doesn't Break", () => {
        expect(threeNumberSum([3, 6, 0, -3], 9)).toEqual(true);
    });

    test("Negative Numbers Before Passing Works - Doesn't Break", () => {
        expect(threeNumberSum([3, 6, -3, 0], 9)).toEqual(true);
    });

    test('Negative Numbers Can Be Used in the Total', () => {
        expect(threeNumberSum([3, 9, -3], 9)).toEqual(true);
    });

    test('First Number Not Included In The Solution', () => {
        expect(threeNumberSum([7, 0, 56, 3, 6, 1], 9)).toEqual(true);
    });

    test("Two Correct Solutions Won't Break", () => {
        expect(threeNumberSum([7, 0, 56, 3, 6, 1, 2], 9)).toEqual(true);
    });

    test("Value Of Null In Array Won't Break", () => {
        expect(threeNumberSum([null, 0, 56, 3, 6, 1, 2], 9)).toEqual(true);
    });

    test('Negative Target Value Works', () => {
        expect(threeNumberSum([-3, -6, 1], -8)).toEqual(true);
    });
});

"""
