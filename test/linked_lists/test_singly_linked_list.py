r"""TODO: port to Python.

Original JavaScript (test/linked-lists/singly-linked-list.test.js):

const { Node, List } = require('../../code/linked-lists/singly-linked-list.js');

describe('singly linked list', () => {
    let list;

    beforeEach(() => {
        list = new List();
    });

    test('push adds nodes to the end', () => {
        list.push(1);
        list.push(2);
        list.push(3);
        expect(list.toArray()).toEqual([1, 2, 3]);
        expect(list.length).toBe(3);
    });

    test('pop removes the last node', () => {
        list.push(1);
        list.push(2);
        const popped = list.pop();
        expect(popped.value).toBe(2);
        expect(list.toArray()).toEqual([1]);
        expect(list.length).toBe(1);

        const popped2 = list.pop();
        expect(popped2.value).toBe(1);
        expect(list.toArray()).toEqual([]);
        expect(list.length).toBe(0);

        const popped3 = list.pop();
        expect(popped3).toBeNull();
    });

    test('delete removes the first occurrence of value', () => {
        list.push(1);
        list.push(2);
        list.push(3);
        list.push(2);

        const deleted = list.delete(2);
        expect(deleted.value).toBe(2);
        expect(list.toArray()).toEqual([1, 3, 2]);
        expect(list.length).toBe(3);

        const deleted2 = list.delete(2);
        expect(deleted2.value).toBe(2);
        expect(list.toArray()).toEqual([1, 3]);
        expect(list.length).toBe(2);

        const deleted3 = list.delete(4);
        expect(deleted3).toBeNull();
    });

    test('find returns the node with given value', () => {
        list.push(1);
        list.push(2);
        list.push(3);

        const node = list.find(2);
        expect(node.value).toBe(2);

        const missing = list.find(4);
        expect(missing).toBeNull();
    });

    test('handles operations on empty list', () => {
        expect(list.pop()).toBeNull();
        expect(list.delete(1)).toBeNull();
        expect(list.find(1)).toBeNull();
        expect(list.toArray()).toEqual([]);
    });
});

"""
