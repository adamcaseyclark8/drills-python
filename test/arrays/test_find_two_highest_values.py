r"""TODO: port to Python.

Original JavaScript (test/arrays/find-two-highest-values.test.js):

const findTwoHighestValues = require('../../code/arrays/find-two-highest-values.js');

// cannot sort the array
// must handle null or empty array
// must handle arrays with less than 2 elements
// must handle duplicate values

describe('find two highest values', () => {
    test('both numbers are both positive', () => {
        expect(findTwoHighestValues([1, 2, 3, 4, 5, 6, 7, 8])).toStrictEqual([8, 7]);
    });

    test('high is positive, second is negative', () => {
        expect(findTwoHighestValues([1, -1, -2, -3])).toStrictEqual([1, -1]);
    });

    test('all numbers in array negative', () => {
        expect(findTwoHighestValues([-1, -2, -3, -4, -5, -6, -7, -8])).toStrictEqual([-1, -2]);
    });

    // test('all numbers in array negative', () => {
    //     expect(findTwoHighestValues([1])).toStrictEqual([-1, -2]);
    // });
    //
    // test('all same number', () => {
    //     expect(findTwoHighestValues([5, 5, 5])).toStrictEqual([]);
    // });
    //
    // test('empty array', () => {
    //     expect(findTwoHighestValues([-1, -2, -3, -4, -5, -6, -7, -8])).toStrictEqual([-1, -2]);
    // });
    //
    // test('null', () => {
    //     expect(findTwoHighestValues([-1, -2, -3, -4, -5, -6, -7, -8])).toStrictEqual([-1, -2]);
    // });
});

"""
