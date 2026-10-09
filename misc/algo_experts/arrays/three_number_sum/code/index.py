r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/three-number-sum/code/index.js):

const threeNumberSum = (numberList, target) => {
    const getTwo = (list, i) => {
        return list[i] + list[i + 1];
    };

    const getThree = (sum, starting, total) => {
        for (let i = 0; i < numberList[starting].length; i++) {
            return sum + numberList[starting + index] === total;
        }
    };

    for (let index = 0; index < numberList.length; index++) {
        if (getTwo(numberList, index)) {
            return getThree(getTwo(numberList, index), index + 2, target);
        }
    }
};

module.exports = threeNumberSum;

"""
