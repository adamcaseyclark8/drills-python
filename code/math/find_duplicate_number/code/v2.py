r"""TODO: port to Python.

Original JavaScript (code/math/find-duplicate-number/code/v2.js):

function findDuplicateNumber(nums) {
    const seen = new Set();
    const duplicates = new Set();

    for (const num of nums) {
        if (seen.has(num)) {
            duplicates.add(num);
        } else {
            seen.add(num);
        }
    }

    return [...duplicates];
}

module.exports = findDuplicateNumber;

"""
