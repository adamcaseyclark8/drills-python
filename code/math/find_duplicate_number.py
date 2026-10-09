r"""TODO: port to Python.

Original JavaScript (code/math/find-duplicate-number.js):

const findDuplicateNumber = nums => {
    const list = [];
    const seen = {};
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (seen[num]) {
            list.push(num);
        }
        seen[num] = true;
    }
    return list.length ? list : -1; // return -1 if no duplicate found
};

module.exports = findDuplicateNumber;

"""
