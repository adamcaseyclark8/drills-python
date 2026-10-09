r"""TODO: port to Python.

Original JavaScript (test/arrays/product-except-self.test.js):

const productExceptSelf = require('../../code/arrays/product-except-self');

test('basic case', () => {
    expect(productExceptSelf([1, 2, 3, 4])).toEqual([24, 12, 8, 6]);
});

test('contains zero', () => {
    expect(productExceptSelf([1, 2, 0, 4])).toEqual([0, 0, 8, 0]);
});

test('two elements', () => {
    expect(productExceptSelf([3, 4])).toEqual([4, 3]);
});

test('all ones', () => {
    expect(productExceptSelf([1, 1, 1, 1])).toEqual([1, 1, 1, 1]);
});

test('single element', () => {
    expect(productExceptSelf([5])).toEqual([1]);
});

test('contains negative numbers', () => {
    expect(productExceptSelf([-1, 2, 3])).toEqual([6, -3, -2]);
});

"""
