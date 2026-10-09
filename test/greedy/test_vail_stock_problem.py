r"""TODO: port to Python.

Original JavaScript (test/greedy/vail-stock-problem.test.js):

const vailStockProblem = require('../../code/greedy/vail-stock-problem.js');

describe('vail stock problem', () => {
    test('I', () => {
        expect(vailStockProblem([500, 750, 1000, 200, 1200, 300, 500])).toStrictEqual(1700);
        // 250, 250, 200,
    });

    test('II', () => {
        expect(vailStockProblem([500, 300, 1000, 100, 1200, 400, 500])).toStrictEqual(1900);
    });

    test('III: first element is highest value', () => {
        expect(vailStockProblem([500, 400, 300, 200, 100])).toStrictEqual(0);
    });

    test('IV', () => {
        expect(vailStockProblem([500, 'two', 300, 200, 100])).toStrictEqual('all values must be numeric');
    });

    test('V', () => {
        expect(vailStockProblem([500, -750, 1000, 200, 1200, 300, 500])).toStrictEqual('all values must be positive');
    });

    test('VI', () => {
        expect(vailStockProblem([])).toStrictEqual(0);
    });

    test('VII', () => {
        expect(vailStockProblem([500])).toStrictEqual(0);
    });

    test('VIII', () => {
        expect(vailStockProblem([500, 1300])).toStrictEqual(800);
    });
});

"""
