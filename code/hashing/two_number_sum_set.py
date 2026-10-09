r"""TODO: port to Python.

Original JavaScript (code/hashing/two-number-sum-set.js):

function twoNumberSumUsingSet(numbers, targetSum) {
    const seen = new Set();
    const results = [];

    for (const number of numbers) {
        const match = targetSum - number;
        if (seen.has(match)) {
            results.push([match, number]);
        }
        seen.add(number);
    }

    return results;
}

module.exports = twoNumberSumUsingSet;

"""
