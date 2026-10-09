r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/longest-range/code/longest-range.js):

// hint: how can you use a hash table to solve this problem with an algorithm that runs in linear time?

function longestRange(array) {
    let best = [];
    let longest = 0;

    const nums = {};

    for (const num of array) {
        nums[num] = true;
    }

    for (const num of array) {
        if (!nums[num]) continue;
        nums[num] = false;

        let current = 1;
        let left = num - 1;
        let right = num + 1;

        while (left in nums) {
            nums[left] = false;
            current++;
            left--;
        }
        while (right in nums) {
            nums[right] = false;
            current++;
            right++;
        }
        if (current > longest) {
            longest = current;

            best = [left + 1, right + 1];
        }
        return best;
    }
}

exports.longestRange = longestRange;

"""
