r"""TODO: port to Python.

Original JavaScript (test/linked-lists/detect-loop-in-a-linked-list.test.js):

const detectLoopInALinkedList = require('../../code/linked-lists/detect-loop-in-a-linked-list.js');

class Node {
    constructor(x) {
        this.data = x;
        this.next = null;
    }
}

describe('verify detect loop in a linked list', () => {
    test('when linked list has loop', () => {
        let head = new Node(1);
        head.next = new Node(3);
        head.next.next = new Node(4);
        head.next.next.next = head.next;

        // 1 => 3 => 4 => 3 (loop)

        expect(detectLoopInALinkedList(head)).toBe(true);
    });

    test('when linked list has no loop', () => {
        let head = new Node(1);
        head.next = new Node(3);
        head.next.next = new Node(4);
        head.next.next.next = new Node(5);

        // 1 => 3 => 4 => 5

        expect(detectLoopInALinkedList(head)).toBe(false);
    });

    test('when list is empty (null head)', () => {
        expect(detectLoopInALinkedList(null)).toBe(false);
    });

    test('when list has a single node with no loop', () => {
        let head = new Node(1);

        expect(detectLoopInALinkedList(head)).toBe(false);
    });

    test('when list has a single node pointing to itself', () => {
        let head = new Node(1);
        head.next = head;

        expect(detectLoopInALinkedList(head)).toBe(true);
    });

    test('when loop is at the tail pointing back to head', () => {
        let head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = head;

        // 1 => 2 => 3 => 1 (loop back to head)

        expect(detectLoopInALinkedList(head)).toBe(true);
    });

    test('when list has two nodes with no loop', () => {
        let head = new Node(1);
        head.next = new Node(2);

        expect(detectLoopInALinkedList(head)).toBe(false);
    });

    test('when list has two nodes with a loop', () => {
        let head = new Node(1);
        head.next = new Node(2);
        head.next.next = head;

        // 1 => 2 => 1 (loop)

        expect(detectLoopInALinkedList(head)).toBe(true);
    });

    test('when loop connects back to a middle node in a longer list', () => {
        let head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = head.next.next; // 5 => 3

        // 1 => 2 => 3 => 4 => 5 => 3 (loop)

        expect(detectLoopInALinkedList(head)).toBe(true);
    });
});

"""
