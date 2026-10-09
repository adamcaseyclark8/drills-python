r"""TODO: port to Python.

Original JavaScript (code/dynamic-programming/best-time-to-buy-and-sell-stock.js):

const bestTimeToBuyAndSellStock = prices => {
    if (!prices || prices.length < 2) return 0;

    let minimum = prices[0];
    let maximum = 0;

    for (let i = 1; i < prices.length; i++) {
        minimum = Math.min(minimum, prices[i]);
        maximum = Math.max(maximum, prices[i] - minimum);
    }

    return maximum;
};

module.exports = bestTimeToBuyAndSellStock;

"""
