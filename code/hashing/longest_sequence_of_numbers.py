r"""TODO: port to Python.

Original JavaScript (code/hashing/longest-sequence-of-numbers.js):

const longestSequenceOfNumbers = nums => {
    const setOfNumbers = new Set(nums);
    let longestSequence = 0;

    for (const num of setOfNumbers) {
        if (!setOfNumbers.has(num - 1)) {
            let currentNum = num;
            let currentSequence = 1;

            while (setOfNumbers.has(currentNum + 1)) {
                currentNum++;
                currentSequence++;
            }

            longestSequence = Math.max(longestSequence, currentSequence);
        }
    }

    return longestSequence;
};

module.exports = longestSequenceOfNumbers;

"""
