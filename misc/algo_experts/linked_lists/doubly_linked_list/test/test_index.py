r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/linked-lists/doubly-linked-list/test/index.test.js):

const { DoublyLinkedList, Node } = require('../code/index');

// class StartNode {
//   constructor(value) {
//     this.value = value;
//     this.previous = null;
//     this.next = null;
//   }
// }
//
// const nodeClass = program.Node || StartNode;
//
// class Node extends nodeClass {
//   constructor(value) {
//     super(value);
//   }
// }

function expectEmpty(linkedList) {
    expect(linkedList.head).toEqual(null);
    expect(linkedList.tail).toEqual(null);
}

function expectHeadTail(linkedList, head, tail) {
    expect(linkedList.head).toEqual(head);
    expect(linkedList.tail).toEqual(tail);
}

function expectSingleNode(linkedList, node) {
    expect(linkedList.head).toEqual(node);
    expect(linkedList.tail).toEqual(node);
}

function getNodeValuesHeadToTail(linkedList) {
    const values = [];
    let node = linkedList.head;
    while (node !== null) {
        values.push(node.value);
        node = node.next;
    }
    return values;
}

function getNodeValuesTailToHead(linkedList) {
    const values = [];
    let node = linkedList.tail;
    while (node !== null) {
        values.push(node.value);
        node = node.previous;
    }
    return values;
}

function removeNodes(linkedList, nodes) {
    for (const node of nodes) {
        linkedList.remove(node);
    }
}

describe('Doubly Linked List Tests', () => {
    let linkedList, node, first, second, third, fourth, fifth, sixth, seventh;

    beforeEach(() => {
        linkedList = DoublyLinkedList();
        first = Node(1);
        second = Node(2);
        third = Node(3);
        fourth = Node(4);
        fifth = Node(5);
        sixth = Node(6);
        seventh = Node(7);
    });

    it('test case #1', () => {
        linkedList.setHead(first);
        expectSingleNode(linkedList, first);
        linkedList.remove(first);
        expectEmpty(linkedList);
        linkedList.setTail(first);
        expectSingleNode(linkedList, first);
        linkedList.removeNodesWithValue(1);
        expectEmpty(linkedList);
        linkedList.insertAtPosition(1, node);
        expectSingleNode(linkedList, node);
    });

    it('test case #2', () => {
        const nodes = [first, second];

        linkedList.setHead(first);
        linkedList.setTail(second);
        expectHeadTail(linkedList, first, second);
        removeNodes(linkedList, nodes);
        expectEmpty(linkedList);

        linkedList.setHead(first);
        linkedList.insertAfter(first, second);
        expectHeadTail(linkedList, first, second);
        removeNodes(linkedList, nodes);
        expectEmpty(linkedList);

        linkedList.setHead(first);
        linkedList.insertBefore(first, second);
        expectHeadTail(linkedList, second, first);
        removeNodes(linkedList, nodes);
        expectEmpty(linkedList);

        linkedList.insertAtPosition(1, first);
        linkedList.insertAtPosition(2, second);
        expectHeadTail(linkedList, first, second);
        removeNodes(linkedList, nodes);
        expectEmpty(linkedList);

        // linkedList.insertAtPosition(2, first);
        // linkedList.insertAtPosition(1, second);
        // expectHeadTail(linkedList, second, first);
    });

    it('test case #3', () => {
        linkedList.setHead(first);
        expect(linkedList.containsNodeWithValue(1)).toBe(true);
        linkedList.insertAfter(first, second);
        expect(linkedList.containsNodeWithValue(2)).toBe(true);
        linkedList.insertAfter(second, third);
        expect(linkedList.containsNodeWithValue(3)).toBe(true);
        linkedList.insertAfter(third, fourth);
        expect(linkedList.containsNodeWithValue(4)).toBe(true);
        linkedList.removeNodesWithValue(3);
        expect(linkedList.containsNodeWithValue(3)).toBe(false);
        linkedList.remove(first);
        expect(linkedList.containsNodeWithValue(1)).toBe(false);
        linkedList.removeNodesWithValue(4);
        expect(linkedList.containsNodeWithValue(4)).toBe(false);
        linkedList.remove(second);
        expect(linkedList.containsNodeWithValue(2)).toBe(false);
    });

    it('test case #4', () => {
        linkedList.setHead(first);
        linkedList.insertAfter(first, second);
        linkedList.insertAfter(second, third);
        linkedList.insertAfter(third, fourth);
        linkedList.insertAfter(fourth, fifth);
        linkedList.insertAfter(fifth, sixth);
        linkedList.insertAfter(sixth, seventh);

        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([1, 2, 3, 4, 5, 6, 7]);
        expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([7, 6, 5, 4, 3, 2, 1]);
        expectHeadTail(linkedList, first, seventh);
        linkedList.remove(second);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([1, 3, 4, 5, 6, 7]);
        expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([7, 6, 5, 4, 3, 1]);
        expectHeadTail(linkedList, first, seventh);
        linkedList.removeNodesWithValue(1);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([3, 4, 5, 6, 7]);
        expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([7, 6, 5, 4, 3]);
        expectHeadTail(linkedList, third, seventh);
        linkedList.removeNodesWithValue(3);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([4, 5, 6, 7]);
        expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([7, 6, 5, 4]);
        expectHeadTail(linkedList, fourth, seventh);
        linkedList.removeNodesWithValue(4);
        linkedList.removeNodesWithValue(5);
        linkedList.removeNodesWithValue(7);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([6]);
        expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([6]);
        expectHeadTail(linkedList, sixth, sixth);
    });

    test('test case #5', () => {
        linkedList.setHead(first);
        linkedList.insertAfter(first, second);
        linkedList.insertAfter(second, third);
        linkedList.insertAfter(third, fourth);

        linkedList.insertAfter(fourth, fifth);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([1, 2, 3, 4, 5]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([5, 4, 3, 2, 1]);
        expectHeadTail(linkedList, first, fifth);

        linkedList.insertAfter(third, fifth);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([1, 2, 3, 5, 4]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([4, 5, 3, 2, 1]);
        expectHeadTail(linkedList, first, fourth);

        linkedList.insertAfter(third, first);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([2, 3, 1, 5, 4]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([4, 5, 1, 3, 2]);
        expectHeadTail(linkedList, second, fourth);

        // linkedList.insertAfter(fifth, second);
        // expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([3, 1, 5, 2, 4]);
        // // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([4, 2, 5, 1, 3]);
        // expectHeadTail(linkedList, third, fourth);

        // linkedList.insertAfter(fourth, sixth);
        // expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([3, 1, 5, 2, 4, 6]);
        // // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([6, 4, 2, 5, 1, 3]);
        // expectHeadTail(linkedList, third, sixth);

        // linkedList.insertAfter(second, seventh);
        // expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([3, 1, 5, 2, 7, 4, 6]);
        // // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([6, 4, 7, 2, 5, 1, 3]);
        // expectHeadTail(linkedList, third, sixth);
    });

    test('test case #6', () => {
        linkedList.setHead(first);
        linkedList.insertBefore(first, second);
        linkedList.insertBefore(second, third);
        linkedList.insertBefore(third, fourth);

        linkedList.insertBefore(fourth, fifth);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([5, 4, 3, 2, 1]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([1,2,3,4,5]);
        expectHeadTail(linkedList, fifth, first);

        linkedList.insertBefore(third, first);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([5, 4, 1, 3, 2]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([2,3,1,4,5]);
        expectHeadTail(linkedList, fifth, second);

        linkedList.insertBefore(fifth, second);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([2, 5, 4, 1, 3]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,1,4,5,2]);
        expectHeadTail(linkedList, second, third);

        // linkedList.insertBefore(fifth, fourth);
        // expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([2,4,5,1,3]);
        // // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,1,5,4,2]);
        // expectHeadTail(linkedList, second, third);

        // linkedList.insertBefore(second, sixth);
        // expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([6,2,4,5,1,3]);
        // // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,1,5,4,2,6]);
        // expectHeadTail(linkedList, sixth, third);

        // linkedList.insertBefore(first, seventh);
        // expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([6,2,4,5,7,1,3]);
        // // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,1,7,5,4,2,6]);
        // expectHeadTail(linkedList, sixth, third);
    });

    test('test case #7', () => {
        linkedList.setHead(first);
        linkedList.insertAtPosition(1, second);
        linkedList.insertAtPosition(1, third);
        linkedList.insertAtPosition(1, fourth);
        linkedList.insertAtPosition(1, fifth);

        const expectedNestedArray = [
            {
                head: [5, 4, 3, 2, 1],
                tail: [1, 2, 3, 4, 5]
            },
            {
                head: [5, 1, 4, 3, 2],
                tail: [2, 3, 4, 1, 5]
            },
            {
                head: [],
                tail: []
            },
            {
                head: [],
                tail: []
            },
            {
                head: [],
                tail: []
            },
            {
                head: [],
                tail: []
            },
            {
                head: [],
                tail: []
            }
        ];

        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual(expectedNestedArray[0].head);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual(expectedNestedArray[0].tail);
        expectHeadTail(linkedList, fifth, first);

        linkedList.insertAtPosition(2, first);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([5, 1, 4, 3, 2]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([2,3,4,1,5]);
        expectHeadTail(linkedList, fifth, second);

        linkedList.insertAtPosition(1, second);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([2, 5, 1, 4, 3]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,4,1,5,2]);
        expectHeadTail(linkedList, second, third);

        linkedList.insertAtPosition(2, fourth);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([2, 4, 5, 1, 3]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,1,5,4,2]);
        expectHeadTail(linkedList, second, third);

        linkedList.insertAtPosition(1, sixth);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([6, 2, 4, 5, 1, 3]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,1,5,4,2,6]);
        expectHeadTail(linkedList, sixth, third);

        linkedList.insertAtPosition(5, seventh);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([6, 2, 4, 5, 7, 1, 3]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([3,1,7,5,4,2,6]);
        expectHeadTail(linkedList, sixth, third);

        linkedList.insertAtPosition(8, fourth);
        expect(getNodeValuesHeadToTail(linkedList)).toStrictEqual([6, 2, 5, 7, 1, 3, 4]);
        // expect(getNodeValuesTailToHead(linkedList)).toStrictEqual([4,3,1,7,5,2,6]);
        expectHeadTail(linkedList, sixth, fourth);
    });
});

"""
