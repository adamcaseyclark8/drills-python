r"""TODO: port to Python.

Original JavaScript (code/strings/code-signal-pyramid-exercise/code/mine.js):

const buildAsciiPyramid = value => {
    const ch = '*';
    const odds = [...Array(value * 2).keys()].filter(n => n % 2 === 1);

    for (let number of odds) {
        const left = Math.floor((21 - number) / 2);
        const right = 21 - number - left;
        const l = ''.repeat(left);
        const c = ch.repeat(number);
        const r = ' '.repeat(right);
        console.log(1 + c + r);
    }
};

module.exports = buildAsciiPyramid;

"""
