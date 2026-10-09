r"""TODO: port to Python.

Original JavaScript (code/hashing/first-repeating-first-missing.js):

const firstRepeatingFirstMissing = numbers => {
    const set = new Set(numbers);
    const seen = new Set();
    let repeating = -1;
    let missing = numbers.length + 1;

    // finds first repeating
    for (const number of numbers) {
        if (seen.has(number)) {
            repeating = number;
            break;
        }
        seen.add(number);
    }

    // calculates first missing
    for (let i = 1; i <= numbers.length; i++) {
        if (!set.has(i)) {
            missing = i;
            break;
        }
    }

    return [repeating, missing];
};

module.exports = firstRepeatingFirstMissing;

"""
