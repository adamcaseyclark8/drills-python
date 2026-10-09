r"""TODO: port to Python.

Original JavaScript (code/hashing/get-all-sum-to-zero.js):

const getAllPairsThatSumToZero = array => {
    const seen = new Set();
    const results = [];
    for (const num of array) {
        if (seen.has(-num)) {
            results.push([Math.min(num, -num), Math.max(num, -num)]);
            seen.delete(-num);
        } else {
            seen.add(num);
        }
    }
    return results;
};

module.exports = getAllPairsThatSumToZero;

// const getAllPairsThatSumToZero = (arr) => {
//     const sorted = [...arr].sort((a, b) => a - b);
//     const results = [];
//     let left = 0, right = sorted.length - 1;
//     while (left < right) {
//         const sum = sorted[left] + sorted[right];
//         if (sum === 0) {
//             results.push([sorted[left], sorted[right]]);
//             left++;
//             right--;
//         } else if (sum < 0) {
//             left++;
//         } else {
//             right--;
//         }
//     }
//     return results;
// };
//
// module.exports = zeroPairs;

"""
