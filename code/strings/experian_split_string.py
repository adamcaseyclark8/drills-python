r"""TODO: port to Python.

Original JavaScript (code/strings/experian-split-string.js):

// from chatgpt

const experianSplitStringFunction = (string, interval) => {
    if (string.length % interval !== 0) {
        return `string is not divisible by ${interval}`;
    }

    const result = [];
    for (let i = 0; i < string.length; i += interval) {
        result.push(string.slice(i, i + interval));
    }
    return result;
};

module.exports = experianSplitStringFunction;

"""
