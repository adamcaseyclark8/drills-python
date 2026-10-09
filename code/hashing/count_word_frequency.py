r"""TODO: port to Python.

Original JavaScript (code/hashing/count-word-frequency.js):

const countWordFrequency = sentence => {
    if (!sentence || sentence.trim().length === 0) return {};

    const map = {};
    const words = sentence.toLowerCase().trim().split(/\s+/);

    for (const word of words) {
        map[word] = (map[word] || 0) + 1;
    }

    return map;
};

module.exports = countWordFrequency;

"""
