r"""TODO: port to Python.

Original JavaScript (code/hashing/get-most-frequent-element.js):

const getMostFrequentElement = array => {
    const map = new Map();
    for (const item of array) map.set(item, (map.get(item) || 0) + 1);
    return [...map.entries()].reduce((a, b) => (b[1] > a[1] ? b : a))[0];
};

module.exports = getMostFrequentElement;

"""
