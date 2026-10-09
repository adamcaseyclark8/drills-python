r"""TODO: port to Python.

Original JavaScript (test/math/expected-goals-scored.test.js):

const expectedGoalsRange = require('../../code/math/expected-goals-scored');

describe('expectedGoalsRange', () => {
    test('returns a single-value range for constant inputs', () => {
        const results = expectedGoalsRange([2, 2, 2], [2, 2, 2], [10, 10, 10], [10, 10, 10]);
        expect(results).toEqual({ low: 2, high: 2 });
    });

    test('returns zero range when all inputs are zero without NaN', () => {
        const results = expectedGoalsRange([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]);
        expect(results).toEqual({ low: 0, high: 0 });
    });

    test('returns integers with low less than or equal to high', () => {
        const results = expectedGoalsRange([1, 3, 0, 2], [2, 1, 4, 1], [12, 15, 8, 11], [9, 14, 13, 10]);
        expect(Number.isInteger(results.low)).toBe(true);
        expect(Number.isInteger(results.high)).toBe(true);
        expect(results.low).toBeLessThanOrEqual(results.high);
    });

    test('never returns a negative low value', () => {
        const results = expectedGoalsRange([0, 6, 0, 6], [0, 6, 0, 6], [10, 10, 10, 10], [10, 10, 10, 10]);
        expect(results.low).toBeGreaterThanOrEqual(0);
    });

    test('weights recent games more heavily', () => {
        const recentHigh = expectedGoalsRange([0, 0, 0, 4], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10]);
        const recentLow = expectedGoalsRange([4, 0, 0, 0], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10]);
        expect(recentHigh.high).toBeGreaterThan(recentLow.high);
    });

    test('treats all games equally when decay is 1', () => {
        const recentHigh = expectedGoalsRange([0, 0, 0, 4], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10], 1);
        const recentLow = expectedGoalsRange([4, 0, 0, 0], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10], 1);
        expect(recentHigh).toEqual(recentLow);
    });

    test('ignores attempts when attemptsWeight is 0', () => {
        const fewAttempts = expectedGoalsRange([1, 2, 3], [2, 2, 2], [5, 5, 5], [5, 5, 5], 0.8, 0);
        const manyAttempts = expectedGoalsRange([1, 2, 3], [2, 2, 2], [30, 30, 30], [30, 30, 30], 0.8, 0);
        expect(fewAttempts).toEqual(manyAttempts);
    });

    test('raises the estimate when the opponent gives up more attempts', () => {
        const results = expectedGoalsRange([2, 2, 2], [2, 2, 2], [10, 10, 10], [30, 30, 30], 0.8, 1);
        expect(results).toEqual({ low: 2, high: 3 });
    });
});
"""
