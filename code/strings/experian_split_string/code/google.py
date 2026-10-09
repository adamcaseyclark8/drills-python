r"""TODO: port to Python.

Original JavaScript (code/strings/experian-split-string/code/google.js):

function experianSplitStingFunction(string, interval) {
    if (string.length % interval !== 0) {
        return `string is not divisible by ${interval}`;
    }

    const numIntervals = Math.ceil(string.length / interval);

    return Array.from({ length: numIntervals }, (v, i) => {
        const start = i * interval;
        const end = start + interval;
        return string.slice(start, end);
    });
}

module.exports = experianSplitStingFunction;

"""
