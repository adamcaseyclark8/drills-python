r"""TODO: port to Python.

Original JavaScript (code/math/find-duplicate-number/code/tortoise.js):

const findDuplicateNumber = nums => {
    // Phase 1: Find the intersection point of the two runners.
    let tortoise = nums[0];
    let hare = nums[0];

    do {
        tortoise = nums[tortoise];
        hare = nums[nums[hare]];
    } while (tortoise !== hare);

    // Phase 2: Find the entrance to the cycle.
    tortoise = nums[0];
    while (tortoise !== hare) {
        tortoise = nums[tortoise];
        hare = nums[hare];
    }

    return hare;
};

module.exports = findDuplicateNumber;

"""
