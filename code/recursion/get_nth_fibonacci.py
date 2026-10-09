r"""TODO: port to Python.

Original JavaScript (code/recursion/get-nth-fibonacci.js):

const getNthFibonacci = nth => {
    const lastTwo = [0, 1];
    let counter = 3;
    while (counter <= nth) {
        [lastTwo[0], lastTwo[1]] = [lastTwo[1], lastTwo[0] + lastTwo[1]];
        counter++;
    }
    return nth > 1 ? lastTwo[1] : lastTwo[0];
};

module.exports = getNthFibonacci;

"""
