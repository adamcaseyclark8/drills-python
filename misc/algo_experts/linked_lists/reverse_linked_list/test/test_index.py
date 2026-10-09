r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/linked-lists/reverse-linked-list/test/index.test.js):

const { reverseLinkedList } = require('../code/index');

class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }

    addMany(values) {
        let current = this;

        while (current.next !== null) {
            current = current.next;
        }

        for (const value of values) {
            current.next = new LinkedList(value);
            current = current.next;
        }
        return this;
    }

    getNodesInArray() {
        const nodes = [];
        let current = this;

        while (current !== null) {
            nodes.push(current.value);
            current = current.next;
        }
        return nodes;
    }
}

describe('Reverse Linked List Tests', () => {
    test('Test Case #1', () => {
        const test = new LinkedList(0);
        const result = reverseLinkedList(test).getNodesInArray();
        const expected = new LinkedList(0).getNodesInArray();
        expect(result).toStrictEqual(expected);
    });

    test('Test Case #2', () => {
        const test = new LinkedList(0).addMany([1]);
        const result = reverseLinkedList(test).getNodesInArray();
        const expected = new LinkedList(1).addMany([0]).getNodesInArray();
        expect(result).toStrictEqual(expected);
    });
});

"""
