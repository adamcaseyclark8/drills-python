r"""TODO: port to Python.

Original JavaScript (code/hashing/first-unique-character.js):

const findFirstUniqueCharacter = string => {
    const freq = {};

    for (let char of string) {
        freq[char] = (freq[char] || 0) + 1;
    }

    for (let i = 0; i < string.length; i++) {
        if (freq[string[i]] === 1) {
            return i;
        }
    }

    return -1;
};

module.exports = findFirstUniqueCharacter;

"""
