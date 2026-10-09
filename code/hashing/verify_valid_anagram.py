r"""TODO: port to Python.

Original JavaScript (code/hashing/verify-valid-anagram.js):

const verifyValidAnagram = (first, second) => {
    if (first.length !== second.length) return false;
    const hashTable = {};

    for (let i = 0; i < first.length; i++) {
        if (!hashTable[first[i]]) {
            hashTable[first[i]] = 0;
        }
        hashTable[first[i]]++;
    }

    for (let j = 0; j < second.length; j++) {
        if (!hashTable[second[j]]) {
            return false;
        }
        hashTable[second[j]]--;
    }

    return true;
};

module.exports = verifyValidAnagram;

"""
