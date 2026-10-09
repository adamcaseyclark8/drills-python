r"""TODO: port to Python.

Original JavaScript (code/backtracking/perform-combination-sum.js):

const performCombinationSum = (candidates, target) => {
    const results = [];

    const backtrack = (remaining, path, start) => {
        if (remaining === 0) {
            results.push([...path]);
            return;
        }

        for (let i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) continue;
            path.push(candidates[i]);
            backtrack(remaining - candidates[i], path, i);
            path.pop();
        }
    };

    backtrack(target, [], 0);
    return results;
};

module.exports = performCombinationSum;

"""
