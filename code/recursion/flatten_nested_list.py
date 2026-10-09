r"""TODO: port to Python.

Original JavaScript (code/recursion/flatten-nested-list.js):

const flattenNestedList = arr => {
    const result = [];

    const flatten = input => {
        for (const item of input) {
            if (Array.isArray(item)) {
                flatten(item);
            } else {
                result.push(item);
            }
        }
    };

    flatten(arr);
    return result;
};

module.exports = flattenNestedList;

"""
