r"""TODO: port to Python.

Original JavaScript (code/math/find-duplicate-number/code/other.js):

function findDuplicateNumber(nums) {
    let slow = nums[0];
    let fast = nums[0];

    // [3, 1, 3, 4, 2]

    // 🔸 First "increment": initialize by moving each pointer forward
    slow = nums[slow]; // 1 step
    fast = nums[nums[fast]]; // 2 steps

    // 🔁 Then continue moving both pointers in a loop
    while (slow !== fast) {
        slow = nums[slow]; // 1 step
        fast = nums[nums[fast]]; // 2 steps
    }

    // 🔁 Second phase: find the start of the cycle
    let start = nums[0];
    while (start !== slow) {
        start = nums[start]; // 1 step
        slow = nums[slow]; // 1 step
    }

    return start;
}

module.exports = findDuplicateNumber;

"""
