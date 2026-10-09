r"""TODO: port to Python.

Original JavaScript (code/math/find-duplicate-number/code/demo.js):

const findDuplicateNumber = numbers => {
    const list = [];
    const set = new Set();

    for (let number of numbers) {
        if (set.has(number)) {
            list.push(number);
        }
        set.add(number);
    }

    return list.length || -1;
};

module.exports = findDuplicateNumber;

"""
