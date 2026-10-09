r"""TODO: port to Python.

Original JavaScript (code/arrays/merge-array-intervals.js):

const mergeArrayIntervals = arrays => {
    if (arrays.length <= 1) return arrays;

    // [[1,3],[2,6],[8,10],[15,18]]

    arrays.sort((a, b) => a[0] - b[0]);
    const result = [arrays[0]];

    for (let i = 1; i < arrays.length; i++) {
        const last = result[result.length - 1];
        const current = arrays[i];

        if (current[0] <= last[1]) {
            last[1] = Math.max(last[1], current[1]);
        } else {
            result.push(current);
        }
    }

    return result;
};

module.exports = mergeArrayIntervals;

"""
