r"""TODO: port to Python.

Original JavaScript (code/two-pointers/find-triplets-with-zero-sum.js):

function findTripletsWithZeroSum(nums) {
    nums.sort((a, b) => a - b); // Sort the array
    const result = [];
    const n = nums.length;

    for (let i = 0; i < n - 2; i++) {
        // Skip duplicate first elements
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const currentSum = nums[i] + nums[left] + nums[right];

            if (currentSum === 0) {
                result.push([nums[i], nums[left], nums[right]]);

                // Skip duplicate second and third elements
                while (left < right && nums[left] === nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] === nums[right - 1]) {
                    right--;
                }

                left++;
                right--;
            } else if (currentSum < 0) {
                left++;
            } else {
                // currentSum > 0
                right--;
            }
        }
    }
    return result;
}

module.exports = findTripletsWithZeroSum;

"""
