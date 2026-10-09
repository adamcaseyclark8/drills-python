r"""TODO: port to Python.

Original JavaScript (code/strings/compress-string-into-char-counts.js):

const compressStringIntoCharCounts = str => {
    if (!str || str.length === 0) return str;

    let compressed = '';
    let count = 1;

    for (let i = 1; i < str.length; i++) {
        if (str[i] === str[i - 1]) {
            count++;
        } else {
            compressed += str[i - 1] + count;
            count = 1;
        }
    }

    // Append the last character and count
    compressed += str[str.length - 1] + count;

    // Return original if compressed is not smaller
    return compressed.length < str.length ? compressed : str;
};

module.exports = compressStringIntoCharCounts;

"""
