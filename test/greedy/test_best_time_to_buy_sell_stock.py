r"""TODO: port to Python.

Original JavaScript (test/greedy/best-time-to-buy-sell-stock.test.js):

const bestTimeToBuySellStock = require('../../code/greedy/best-time-to-buy-sell-stock.js');

describe('test cases for max profit', () => {
    test('returns max profit for typical increasing then decreasing prices', () => {
        expect(bestTimeToBuySellStock([7, 1, 5, 3, 6, 4])).toBe(5);
    });

    test('returns 0 when prices only decrease', () => {
        expect(bestTimeToBuySellStock([7, 6, 4, 3, 1])).toBe(0);
    });

    test('returns 0 for empty array', () => {
        expect(bestTimeToBuySellStock([])).toBe(0);
    });

    test('returns 0 for single price', () => {
        expect(bestTimeToBuySellStock([5])).toBe(0);
    });

    test('returns correct profit when best buy/sell are at the ends', () => {
        expect(bestTimeToBuySellStock([2, 4, 1, 7])).toBe(6);
    });

    test('handles all equal prices', () => {
        expect(bestTimeToBuySellStock([3, 3, 3, 3])).toBe(0);
    });
});

"""
