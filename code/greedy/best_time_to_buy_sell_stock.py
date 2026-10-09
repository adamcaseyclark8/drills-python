r"""TODO: port to Python.

Original JavaScript (code/greedy/best-time-to-buy-sell-stock.js):

const bestTimeToBuySellStock = numbers => {
    let minPrice = Infinity;
    let result = 0;

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] < minPrice) {
            minPrice = numbers[i];
        } else if (numbers[i] - minPrice > result) {
            result = numbers[i] - minPrice;
        }
    }

    return result;
};

module.exports = bestTimeToBuySellStock;

"""
