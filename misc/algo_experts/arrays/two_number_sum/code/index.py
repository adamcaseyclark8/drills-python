r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/two-number-sum/code/index.js):

// v1 - time: O(n^2) | space: O(1)
// runs first element in parent array
// loops all in nested array
// stops after it finds

// function twoNumberSum(array, targetSum) {
//   for (let i = 0; i < array.length - 1; i++) {
//     const firstNum = array[i];
//
//     console.log("firstNum");
//     console.log(firstNum);
//
//     for (let j = i + 1; j < array.length; j++) {
//       const secondNum = array[j];
//
//       console.log("secondNum");
//       console.log(secondNum);
//
//       if (firstNum + secondNum === targetSum) {
//         return [firstNum, secondNum];
//       }
//     }
//   }
//   return [];
// }

// v2 - time: O(n) | space: O(n)
// loops over array subtracts element from target

function twoNumberSum(array, targetSum) {
    const nums = {};
    for (const num of array) {
        const potentialMatch = targetSum - num;
        if (potentialMatch in nums) {
            return [potentialMatch, num];
        } else {
            nums[num] = true;
        }
    }

    return [];
}

// v3 - time: O(nlog(n)) | space: O(1)

// function twoNumberSum(array, targetSum) {
//   array.sort((a, b) => a - b);
//   let left = 0;
//   let right = array.length - 1;
//
//   while (left < right) {
//     const currentSum = array[left] + array[right];
//     if (currentSum === targetSum) {
//       return [array[left], array[right]];
//     } else if (currentSum < targetSum) {
//       left++;
//     } else if (currentSum > targetSum) {
//       right--;
//     }
//   }
//   return [];
// }

exports.twoNumberSum = twoNumberSum;

"""
