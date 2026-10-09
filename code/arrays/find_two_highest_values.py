r"""TODO: port to Python.

Original JavaScript (code/arrays/find-two-highest-values.js):

const findTwoHighestValues = numbers => {
    let highest = -Infinity;
    let second = -Infinity;

    for (let number of numbers) {
        if (number > highest) {
            second = highest;
            highest = number;
        } else if (number > second) {
            second = number;
        }
    }

    return [highest, second];
};

module.exports = findTwoHighestValues;

"""
