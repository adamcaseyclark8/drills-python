r"""TODO: port to Python.

Original JavaScript (test/dynamic-programming/find-number-of-coin-combinations.test.js):

const findNumberOfCoinCombinations = require('../../code/dynamic-programming/find-number-of-coin-combinations');

describe('find number of coin combinations tests', () => {
    test('example case - amount 5, coins [1,2,5]', () => {
        expect(findNumberOfCoinCombinations(5, [1, 2, 5])).toBe(4);
    });

    test('no combinations possible', () => {
        expect(findNumberOfCoinCombinations(3, [2])).toBe(0);
    });

    test('amount is zero - one way (use nothing)', () => {
        expect(findNumberOfCoinCombinations(0, [1, 2, 5])).toBe(1);
    });

    test('single coin that divides evenly', () => {
        expect(findNumberOfCoinCombinations(6, [3])).toBe(1);
    });

    test('single coin that does not divide evenly', () => {
        expect(findNumberOfCoinCombinations(7, [3])).toBe(0);
    });

    test('all ones - only one combination', () => {
        expect(findNumberOfCoinCombinations(4, [1])).toBe(1);
    });

    test('larger amount', () => {
        expect(findNumberOfCoinCombinations(10, [1, 2, 5])).toBe(10);
    });

    test('order does not matter - combinations not permutations', () => {
        expect(findNumberOfCoinCombinations(4, [1, 2])).toBe(3);
    });
});

"""
