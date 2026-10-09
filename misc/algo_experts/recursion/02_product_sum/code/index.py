r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/recursion/02-product-sum/code/index.js):

function productSum(array, multiplier = 1) {
    let sum = 0;

    for (const element of array) {
        if (Array.isArray(element)) {
            sum += productSum(element, multiplier + 1);
        } else {
            sum += element;
        }
    }
    return sum * multiplier;
}

exports.productSum = productSum;

"""
