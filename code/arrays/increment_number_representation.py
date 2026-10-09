r"""TODO: port to Python.

Original JavaScript (code/arrays/increment-number-representation.js):

const incrementNumberRepresentation = digits => {
    const result = [...digits];

    // LAST DIGIT IN ARRAY FIRST
    // MOVING LEFT TO RIGHT
    // WHILE INDEX IS GREATER THAN OR EQUAL TO ZERO

    for (let i = result.length - 1; i >= 0; i--) {
        if (result[i] < 9) {
            result[i]++;
            return result;
        }
        result[i] = 0;
    }

    // All digits were 9, prepend a 1
    return [1, ...result];
};

module.exports = incrementNumberRepresentation;

"""
