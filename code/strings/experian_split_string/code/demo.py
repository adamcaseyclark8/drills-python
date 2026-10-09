r"""TODO: port to Python.

Original JavaScript (code/strings/experian-split-string/code/demo.js):

const experianSplitStingFunction = (string, interval) => {
    const result = [];
    if (string.length % interval !== 0) {
        return `string is not divisible by ${interval}`;
    }

    for (let int = 0; int < string.length; int += interval) {
        // console.log(int, int + interval)

        // 03 47

        result.push(string.slice(int, int + interval));
    }

    return result;
};

// experianSplitStingFunction('adamcaseyclarkxx', 4)
// console.log(experianSplitStingFunction('adamcaseyclarkxx', 4))

module.exports = experianSplitStingFunction;

"""
