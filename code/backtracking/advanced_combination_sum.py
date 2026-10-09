r"""TODO: port to Python.

Original JavaScript (code/backtracking/advanced-combination-sum.js):

const performAdvancedCombinationSum = (candidates, target) => {
    const result = [];
    candidates.sort((a, b) => a - b);

    const dfs = (start, current, remaining) => {
        if (remaining === 0) {
            result.push([...current]);
            return;
        }
        for (let i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) break;
            if (i > start && candidates[i] === candidates[i - 1]) continue;
            current.push(candidates[i]);
            dfs(i + 1, current, remaining - candidates[i]);
            current.pop();
        }
    };

    dfs(0, [], target);
    return result;
};

module.exports = performAdvancedCombinationSum;

"""
