r"""TODO: port to Python.

Original JavaScript (code/dynamic-programming/find-number-of-coin-combinations.js):

const findNumberOfCoinCombinations = (amount, coins) => {
    const dp = new Array(amount + 1).fill(0);
    dp[0] = 1;

    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] += dp[i - coin];
        }
    }

    return dp[amount];
};

module.exports = findNumberOfCoinCombinations;

"""
