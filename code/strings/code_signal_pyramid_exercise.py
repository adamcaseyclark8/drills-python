r"""TODO: port to Python.

Original JavaScript (code/strings/code-signal-pyramid-exercise.js):

// from claude

const buildAsciiPyramid = n => {
    for (let i = 1; i <= n; i++) {
        const spaces = ' '.repeat(n - i);
        const asterisks = '*'.repeat(2 * i - 1);
        console.log(spaces + asterisks);
    }
};

module.exports = buildAsciiPyramid;

"""
