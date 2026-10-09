r"""TODO: port to Python.

Original JavaScript (code/backtracking/permutations-of-an-array.js):

const permutationsOfAnArray = nums => {
    const results = [];

    const backtrack = (path, remaining) => {
        if (remaining.length === 0) {
            results.push([...path]);
            return;
        }

        for (let i = 0; i < remaining.length; i++) {
            path.push(remaining[i]);
            backtrack(path, [...remaining.slice(0, i), ...remaining.slice(i + 1)]);
            path.pop();
        }
    };

    backtrack([], nums);
    return results;
};

module.exports = permutationsOfAnArray;

"""
