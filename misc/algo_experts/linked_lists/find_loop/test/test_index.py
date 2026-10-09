r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/linked-lists/find-loop/test/index.test.js):

const { LinkedList, findLoop } = require('../code/index');

class StartLinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

const linkedListClass = LinkedList || StartLinkedList;

class LinkedListImplementation extends linkedListClass {
    constructor(value) {
        super(value);
    }

    addMany(values) {
        let current = this;

        while (current.next !== null) {
            current = current.next;
        }

        for (const value of values) {
            current.next = new LinkedListImplementation(value);
            current = current.next;
        }
        return this;
    }

    getNthNode(n) {
        let counter = 1;
        let current = this;

        while (counter < n) {
            current = current.next;
            counter++;
        }
        return current;
    }
}

describe('Find Loop Tests, Linked List', () => {
    test('Test Case #1', () => {
        const test1 = new LinkedListImplementation(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9]);

        console.log(LinkedListImplementation);

        test1.getNthNode(10).next = test1.getNthNode(1);
        expect(findLoop(test1)).toStrictEqual(test1.getNthNode(1));
    });

    test('Test Case #2', () => {
        const test2 = new LinkedListImplementation(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9]);

        test2.getNthNode(10).next = test2.getNthNode(2);
        expect(findLoop(test2)).toStrictEqual(test2.getNthNode(2));
    });
});

"""
