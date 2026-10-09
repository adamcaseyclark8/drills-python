r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/two-number-sum/code/als-version.js):

const twoSum = (smallerTargetSum, start) => {
    const x = {};
    for (let i = start; i < arr.length; i += 1) {
        const num = arr[i];
        if (x[num]) {
            return true;
        }
        x[smallerTargetSum - num] = true;
    }
    return false;
};

"""
