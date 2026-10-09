r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/three-number-sum/test/index.test.js):

// const program = require("../code/index");
const program = require('../code/als-version');
const chai = require('chai');

test('An Array With Less Than 3 Numbers Returns False', () => {
    chai.expect(program.threeNumberSum([3, 6], 9)).to.equal(false);
});

test("3 Numbers That Does Add Up Doesn't Work", () => {
    chai.expect(program.threeNumberSum([1, 2, 3], 7)).to.equal(false);
});

test('4 Numbers That Sums To Target Returns False', () => {
    chai.expect(program.threeNumberSum([1, 2, 3, 4], 10)).to.equal(false);
});

test('Three Numbers Works', () => {
    chai.expect(program.threeNumberSum([3, 5, 1], 9)).to.equal(true);
});

test('Array Can Be Include Zero', () => {
    chai.expect(program.threeNumberSum([3, 6, 0], 9)).to.equal(true);
});

test('Duplicated Numbers In The Array Works', () => {
    chai.expect(program.threeNumberSum([3, 6, 0, 3], 9)).to.equal(true);
});

test("Negative Numbers After Passing Works - Doesn't Break", () => {
    chai.expect(program.threeNumberSum([3, 6, 0, -3], 9)).to.equal(true);
});

test("Negative Numbers Before Passing Works - Doesn't Break", () => {
    chai.expect(program.threeNumberSum([3, 6, -3, 0], 9)).to.equal(true);
});

test('Negative Numbers Can Be Used in the Total', () => {
    chai.expect(program.threeNumberSum([3, 9, -3], 9)).to.equal(true);
});

test('First Number Not Included In The Solution', () => {
    chai.expect(program.threeNumberSum([7, 0, 56, 3, 6, 1], 9)).to.equal(true);
});

test("Two Correct Solutions Won't Break", () => {
    chai.expect(program.threeNumberSum([7, 0, 56, 3, 6, 1, 2], 9)).to.equal(true);
});

test("Value Of Null In Array Won't Break", () => {
    chai.expect(program.threeNumberSum([null, 0, 56, 3, 6, 1, 2], 9)).to.equal(true);
});

test('Negative Target Value Works', () => {
    chai.expect(program.threeNumberSum([-3, -6, 1], -8)).to.equal(true);
});

"""
