r"""TODO: port to Python.

Original JavaScript (code/hashing/contains-duplicates.js):

const arrayContainsDuplicates = arr => {
    const seen = {};
    for (let i = 0; i < arr.length; i++) {
        const value = arr[i];
        if (seen[value]) return true;
        seen[value] = true;
    }
    return false;
};

module.exports = arrayContainsDuplicates;

"""
