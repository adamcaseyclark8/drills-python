r"""TODO: port to Python.

Original JavaScript (code/two-pointers/move-zeroes-right.js):

const moveZeroesRight = numbers => {
    let lastNonZeroFoundAt = 0;

    // Move all non-zero elements to the beginning
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] !== 0) {
            numbers[lastNonZeroFoundAt] = numbers[i];
            lastNonZeroFoundAt++;
        }
    }

    // Fill the rest with zeros
    for (let i = lastNonZeroFoundAt; i < numbers.length; i++) {
        numbers[i] = 0;
    }

    return numbers; // Or modify the array in-place without returning
};

module.exports = moveZeroesRight;

"""
