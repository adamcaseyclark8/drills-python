r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/two-number-sum/test/index.test.js):

// const program = require("../code/index");
const program = require('../code/index');
const chai = require('chai');

test('Sample Input Works', () => {
    chai.expect(program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)).to.have.members([-1, 11]);
});

test('Test Case #01', () => {
    const output = program.twoNumberSum([4, 6], 10).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([4, 6]);
});

test('Test Case #02', () => {
    const output = program.twoNumberSum([4, 6, 1], 5).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([1, 4]);
});

test('Test Case #03.v3.functions', () => {
    const output = program.twoNumberSum([4, 6, 1, -3], 3).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([-3, 6]);
});

test('Test Case #04', () => {
    const output = program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([-1, 11]);
});

test('Test Case #05', () => {
    const output = program.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([8, 9]);
});

test('Test Case #06', () => {
    const output = program.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([3, 15]);
});

test('Test Case #07', () => {
    const output = program.twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([-5, 0]);
});

test('Test Case #08', () => {
    const output = program.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([-47, 210]);
});

test('Test Case #09', () => {
    const output = program.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([]);
});

test('Test Case #10', () => {
    const output = program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15).sort((a, b) => a - b);

    chai.expect(output).to.deep.equal([]);
});

"""
