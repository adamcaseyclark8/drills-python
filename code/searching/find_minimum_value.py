r"""TODO: port to Python.

Original JavaScript (code/searching/find-minimum-value.js):

const findMinimumValue = array => {
    // Assume the first element is the minimum
    let min = array[0];
    for (let i = 1; i < array.length; i++) {
        if (array[i] < min) {
            // Update min if a smaller value is found
            min = array[i];
        }
    }
    return min;
};

module.exports = findMinimumValue;

"""
