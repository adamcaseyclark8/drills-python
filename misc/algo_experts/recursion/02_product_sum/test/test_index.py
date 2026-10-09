r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/recursion/02-product-sum/test/index.test.js):

// const program = require("../code/index");
const program = require('../code/index');
const chai = require('chai');

test('Sample Input Gets Sample Output', () => {
    const test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]];
    chai.expect(program.productSum(test)).to.deep.equal(12);
});

test('Test Case #1', () => {
    const test = [1, 2, 3, 4, 5];
    chai.expect(program.productSum(test)).to.deep.equal(15);
});

test('Test Case #2', () => {
    const test = [1, 2, [3], 4, 5];
    chai.expect(program.productSum(test)).to.deep.equal(18);
});

test('Test Case #3', () => {
    const test = [[1, 2], 3, [4, 5]];
    chai.expect(program.productSum(test)).to.deep.equal(27);
});

"""
