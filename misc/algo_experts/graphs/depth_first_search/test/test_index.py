r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/graphs/depth-first-search/test/index.test.js):

const program = require('../code/index');
const chai = require('chai');

const test1 = new program.Node('A');
test1.addChild('B').addChild('C');
test1.children[0].addChild('D');

const test2 = new program.Node('A');

test2.addChild('B').addChild('C').addChild('D').addChild('E');
test2.children[1].addChild('F');

const test3 = new program.Node('A');

const test4 = new program.Node('A');
const test5 = new program.Node('A');

it('Test Case #1', function () {
    chai.expect(test1.depthFirstSearch([])).to.deep.equal(['A', 'B', 'D', 'C']);
});

it('Test Case #2', function () {
    chai.expect(test2.depthFirstSearch([])).to.deep.equal(['A', 'B', 'C', 'F', 'D', 'E']);
});

it('Test Case #3', () => {});

"""
