r"""TODO: port to Python.

Original JavaScript (test/dynamic-programming/get-least-number-of-coins.test.js):

const getLeastNumberOfCoins = require('../../code/dynamic-programming/get-least-number-of-coins.js');

describe('getLeastNumberOfCoins', () => {
    test('[1,5,10,25], amount 36 returns 3', () => {
        expect(getLeastNumberOfCoins([1, 5, 10, 25], 36)).toBe(3);
    });

    test('[1,2,5], amount 11 returns 3', () => {
        expect(getLeastNumberOfCoins([1, 2, 5], 11)).toBe(3);
    });

    test('[2], amount 3 returns -1', () => {
        expect(getLeastNumberOfCoins([2], 3)).toBe(-1);
    });

    test('[1], amount 0 returns 0', () => {
        expect(getLeastNumberOfCoins([1], 0)).toBe(0);
    });

    test('[1], amount 1 returns 1', () => {
        expect(getLeastNumberOfCoins([1], 1)).toBe(1);
    });

    test('[1], amount 5 returns 5', () => {
        expect(getLeastNumberOfCoins([1], 5)).toBe(5);
    });

    test('exact match returns 1', () => {
        expect(getLeastNumberOfCoins([5, 10, 25], 25)).toBe(1);
    });

    test('no solution returns -1', () => {
        expect(getLeastNumberOfCoins([5, 10], 3)).toBe(-1);
    });
});

"""
