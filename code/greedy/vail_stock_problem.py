r"""TODO: port to Python.

Original JavaScript (code/greedy/vail-stock-problem.js):

const vailStockProblem = numbers => {
    const profits = [];
    let current = numbers[0];

    for (let i = 0; i < numbers.length; i++) {
        if (typeof numbers[i] === 'string') {
            return 'all values must be numeric';
        }

        if (numbers[i] < 0) {
            return 'all values must be positive';
        }

        if (numbers[i - 1] > numbers[i]) {
            profits.push(numbers[i - 1] - current);
            current = numbers[i];
        } else if (i === numbers.length - 1) {
            profits.push(numbers[i] - current);
        }
    }

    return profits.length === 0 ? 0 : profits.reduce((current, value) => current + value, 0);
};

module.exports = vailStockProblem;

// console.log(vailStockProblem([500, 750, 1000, 200, 1200, 300, 500]));
// console.log(vailStockProblem([500, 300, 1000, 100, 1200, 400, 500]));
// console.log(vailStockProblem([500, 400, 300, 200, 100]));
// console.log(vailStockProblem([1500, 'two', 300, 200, 100]));
// console.log(vailStockProblem([500, -750, 1000, 200, 1200, 300, 500]));
// console.log(vailStockProblem([]));
// console.log(vailStockProblem([500]));
// console.log(vailStockProblem([500, 1300]));

"""
