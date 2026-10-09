r"""TODO: port to Python.

Original JavaScript (test/linked-lists/find-middle-node-of-list.test.js):

// solution.test.js

const { findMiddleNode, buildList, listToArray } = require('../../code/linked-lists/find-middle-node-of-list.js');

describe('findMiddleNode', () => {
    describe('odd length lists', () => {
        test('[1, 2, 3] → middle is 2', () => {
            const result = findMiddleNode(buildList([1, 2, 3]));
            expect(result.val).toBe(2);
        });

        test('[1, 2, 3, 4, 5] → middle is 3', () => {
            const result = findMiddleNode(buildList([1, 2, 3, 4, 5]));
            expect(result.val).toBe(3);
        });

        test('[10, 20, 30, 40, 50, 60, 70] → middle is 40', () => {
            const result = findMiddleNode(buildList([10, 20, 30, 40, 50, 60, 70]));
            expect(result.val).toBe(40);
        });
    });

    describe('even length lists — returns second middle node', () => {
        test('[1, 2] → middle is 2', () => {
            const result = findMiddleNode(buildList([1, 2]));
            expect(result.val).toBe(2);
        });

        test('[1, 2, 3, 4] → middle is 3', () => {
            const result = findMiddleNode(buildList([1, 2, 3, 4]));
            expect(result.val).toBe(3);
        });

        test('[1, 2, 3, 4, 5, 6] → middle is 4', () => {
            const result = findMiddleNode(buildList([1, 2, 3, 4, 5, 6]));
            expect(result.val).toBe(4);
        });
    });

    describe('the returned node still points to the rest of the list', () => {
        test('[1, 2, 3, 4, 5] → middle node tail is [3, 4, 5]', () => {
            const result = findMiddleNode(buildList([1, 2, 3, 4, 5]));
            expect(listToArray(result)).toEqual([3, 4, 5]);
        });

        test('[1, 2, 3, 4] → middle node tail is [3, 4]', () => {
            const result = findMiddleNode(buildList([1, 2, 3, 4]));
            expect(listToArray(result)).toEqual([3, 4]);
        });
    });

    describe('edge cases', () => {
        test('single node [1] → middle is 1', () => {
            const result = findMiddleNode(buildList([1]));
            expect(result.val).toBe(1);
        });

        test('null head → returns null', () => {
            expect(findMiddleNode(null)).toBeNull();
        });
    });
});

"""
