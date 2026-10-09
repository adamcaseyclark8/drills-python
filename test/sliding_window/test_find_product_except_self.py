r"""TODO: port to Python.

Original JavaScript (test/sliding-window/find-product-except-self.test.js):

const findProductExceptSelf = require('../../code/sliding-window/find-product-except-self.js');

describe('find product except self tests', () => {
    test('[1,2,3,4] returns [24,12,8,6]', () => {
        expect(findProductExceptSelf([1, 2, 3, 4])).toEqual([24, 12, 8, 6]);
    });

    // test('[-1,1,0,-3,3] returns [0,0,9,0,0]', () => {
    //     expect(findProductExceptSelf([-1, 1, 0, -3, 3])).toEqual([0, 0, 9, 0, 0]);
    // });

    test('two elements returns reversed values', () => {
        expect(findProductExceptSelf([3, 4])).toEqual([4, 3]);
    });

    test('array with a zero', () => {
        expect(findProductExceptSelf([1, 0, 3])).toEqual([0, 3, 0]);
    });

    test('array with two zeros returns all zeros', () => {
        expect(findProductExceptSelf([0, 0, 3])).toEqual([0, 0, 0]);
    });

    test('all ones returns all ones', () => {
        expect(findProductExceptSelf([1, 1, 1, 1])).toEqual([1, 1, 1, 1]);
    });

    test('negative numbers', () => {
        expect(findProductExceptSelf([-2, -3, -4])).toEqual([12, 8, 6]);
    });
});

"""
