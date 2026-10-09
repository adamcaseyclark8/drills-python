r"""TODO: port to Python.

Original JavaScript (test/dynamic-programming/best-time-to-buy-and-sell-stock.test.js):

const bestTimeToBuyAndSellStock = require('../../code/dynamic-programming/best-time-to-buy-and-sell-stock.js');

describe('best time to buy and sell stock test (dynamic programming)', () => {
    test('returns max profit for standard case', () => {
        expect(bestTimeToBuyAndSellStock([7, 1, 5, 3, 6, 4])).toBe(5);
    });

    test('returns 0 when prices only decrease', () => {
        expect(bestTimeToBuyAndSellStock([7, 6, 4, 3, 1])).toBe(0);
    });

    test('returns profit when best buy is first element', () => {
        expect(bestTimeToBuyAndSellStock([1, 2, 3, 4, 5])).toBe(4);
    });

    test('returns profit for two-element array', () => {
        expect(bestTimeToBuyAndSellStock([1, 5])).toBe(4);
    });

    test('returns 0 for two equal prices', () => {
        expect(bestTimeToBuyAndSellStock([3, 3])).toBe(0);
    });

    test('returns 0 for single element', () => {
        expect(bestTimeToBuyAndSellStock([5])).toBe(0);
    });

    test('returns 0 for empty array', () => {
        expect(bestTimeToBuyAndSellStock([])).toBe(0);
    });

    test('handles valley before peak mid-array', () => {
        expect(bestTimeToBuyAndSellStock([3, 10, 1, 9])).toBe(8);
    });
});

"""
