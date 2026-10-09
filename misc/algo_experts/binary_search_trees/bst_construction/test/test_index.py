r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/binary-search-trees/bst-construction/test/index.test.js):

const program = require('../code/index');
const chai = require('chai');

const test1 = new program.BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22);

const test2 = new program.BST(10).insert(15).insert(11).insert(22).remove(10);

const test3 = new program.BST(10).insert(5).insert(7).insert(2).remove(10);

const test4 = new program.BST(10)
    .insert(5)
    .insert(15)
    .insert(22)
    .insert(17)
    .insert(34)
    .insert(7)
    .insert(2)
    .insert(5)
    .insert(1)
    .insert(35)
    .insert(27)
    .insert(16)
    .insert(30)
    .insert(22)
    .insert(17);

function inOrderTraverse(tree, array) {
    if (tree !== null) {
        inOrderTraverse(tree.left, array);
        array.push(tree.value);
        inOrderTraverse(tree.right, array);
    }
    return array;
}

it('Test Case #1', function () {
    chai.expect(test1.left.value).to.deep.equal(5);
});

it('Test Case #2', function () {
    chai.expect(test1.right.right.value).to.deep.equal(22);
});

it('Test Case #3', function () {
    chai.expect(test1.right.left.value).to.deep.equal(14);
});

it('Test Case #4', function () {
    chai.expect(test1.left.right.value).to.deep.equal(5);
});

it('Test Case #5', function () {
    chai.expect(test1.left.left.value).to.deep.equal(2);
});

it('Test Case #6', function () {
    chai.expect(test1.left.left.left).to.deep.equal(null);
});

it('Test Case #7', function () {
    chai.expect(test1.right.left.right).to.deep.equal(null);
});

it('Test Case #8', function () {
    chai.expect(test1.contains(15)).to.equal(true);
});

it('Test Case #9', function () {
    chai.expect(test1.contains(2)).to.equal(true);
});

it('Test Case #10', function () {
    chai.expect(test1.contains(5)).to.equal(true);
});

it('Test Case #11', function () {
    chai.expect(test1.contains(10)).to.equal(true);
});

it('Test Case #12', function () {
    chai.expect(test1.contains(22)).to.equal(true);
});

it('Test Case #13', function () {
    chai.expect(test1.contains(23)).to.equal(false);
});

it('Test Case #14', function () {
    chai.expect(inOrderTraverse(test2, [])).to.deep.equal([11, 15, 22]);
});

// it("Test Case #15", function() {
//   chai.expect().to.deep.equal();
// });
//
// it("Test Case #16", function() {
//   chai.expect().to.deep.equal();
// });
//
// it("Test Case #17", function() {
//   chai.expect().to.deep.equal();
// });
//
// it("Test Case #18", function() {
//   chai.expect().to.deep.equal();
// });

"""
