r"""TODO: port to Python.

Original JavaScript (code/hashing/remove-all-duplicates.js):

function removeAllDuplicates(array) {
    const seen = {};
    const result = [];

    for (let i = 0; i < array.length; i++) {
        const item = array[i];
        if (!seen[item]) {
            seen[item] = true;
            result.push(item);
        }
    }

    return result;
}

module.exports = removeAllDuplicates;

"""
