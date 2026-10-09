r"""TODO: port to Python.

Original JavaScript (code/arrays/product-except-self.js):

const productExceptSelf = array => {
    const results = new Array(array.length).fill(1);
    let prefix = 1;
    for (let i = 0; i < array.length; i++) {
        results[i] = prefix;
        prefix *= array[i];
    }
    let suffix = 1;
    for (let i = array.length - 1; i >= 0; i--) {
        results[i] *= suffix;
        suffix *= array[i];
    }
    return results;
};

module.exports = productExceptSelf;

"""
