r"""TODO: port to Python.

Original JavaScript (code/sliding-window/chunk-array-into-groups.js):

const chunkArrayIntoGroups = (array, size) => {
    const results = [];
    for (let i = 0; i < array.length; i += size) {
        results.push(array.slice(i, i + size));
    }
    return results;
};

module.exports = chunkArrayIntoGroups;

"""
