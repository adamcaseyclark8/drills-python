r"""TODO: port to Python.

Original JavaScript (code/hashing/two-number-sum-map.js):

const twoNumberSumUsingMap = (numbers, target) => {
    const map = new Map();
    for (let i = 0; i < numbers.length; i++) {
        const complement = target - numbers[i];
        if (map.has(complement)) return [map.get(complement), i];
        map.set(numbers[i], i);
    }
};

module.exports = twoNumberSumUsingMap;

"""
