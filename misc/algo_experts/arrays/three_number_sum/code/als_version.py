r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/three-number-sum/code/als-version.js):

const threeNumberSum = (arr, targetSum) => {
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

    for (let i = 0; i < arr.length - 2; i += 1) {
        // console.log(twoSum(targetSum - arr[i], i + 1))

        if (twoSum(targetSum - arr[i], i + 1)) {
            return true;
        }
    }
    return false;
};

module.exports = threeNumberSum;

"""
