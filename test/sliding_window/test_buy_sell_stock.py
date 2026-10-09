r"""TODO: port to Python.

Original JavaScript (test/sliding-window/buy-sell-stock.test.js):

const bestTimeToBuyOrSellStock = require('../../code/sliding-window/buy-sell-stock.js');

describe('verify best time to buy sell stock', () => {
    test('misc scenario', () => {
        expect(bestTimeToBuyOrSellStock([7, 1, 5, 3, 6, 4])).toBe(5);
    });

    test('Example case: increasing prices', () => {
        expect(bestTimeToBuyOrSellStock([7, 1, 5, 3, 6, 4])).toBe(5); // Buy at 1, sell at 6
    });

    test('Example case: decreasing prices', () => {
        expect(bestTimeToBuyOrSellStock([7, 6, 4, 3, 1])).toBe(0); // No profit possible
    });

    test('Empty array', () => {
        expect(bestTimeToBuyOrSellStock([])).toBe(0);
    });

    test('Single day price', () => {
        expect(bestTimeToBuyOrSellStock([5])).toBe(0); // Cannot sell
    });

    test('Prices remain constant', () => {
        expect(bestTimeToBuyOrSellStock([3, 3, 3, 3, 3])).toBe(0);
    });

    test('Large profit late in array', () => {
        expect(bestTimeToBuyOrSellStock([10, 2, 1, 5, 6, 20])).toBe(19); // Buy at 1, sell at 20
    });

    test('Profit happens after multiple drops', () => {
        expect(bestTimeToBuyOrSellStock([9, 7, 4, 1, 5, 8])).toBe(7); // Buy at 1, sell at 8
    });

    test('Two elements increasing', () => {
        expect(bestTimeToBuyOrSellStock([2, 4])).toBe(2);
    });

    test('Two elements decreasing', () => {
        expect(bestTimeToBuyOrSellStock([5, 3])).toBe(0);
    });

    test('Multiple peaks and valleys', () => {
        expect(bestTimeToBuyOrSellStock([3, 2, 6, 1, 4])).toBe(4); // Buy at 2, sell at 6
    });
});

"""
