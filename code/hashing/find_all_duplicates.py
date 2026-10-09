r"""TODO: port to Python.

Original JavaScript (code/hashing/find-all-duplicates.js):

const findAllDuplicates = nums => {
    const seen = new Set();
    const duplicates = [];

    for (const num of nums) {
        if (seen.has(num)) {
            duplicates.push(num);
        } else {
            seen.add(num);
        }
    }

    return duplicates;
};

module.exports = findAllDuplicates;

"""
