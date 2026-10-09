r"""TODO: port to Python.

Original JavaScript (test/structures/priority-queue/queue.test.js):

const Queue = require('../../../code/structures/priority-queue/queue');

// IMPLEMENT QUEUE METHODS:
// ENQUEUE, DEQUEUE, PEEK, TO ARRAY

describe('queue test cases', () => {
    let queue;

    beforeEach(() => {
        queue = new Queue();
    });

    test('enqueue adds elements to the end', () => {
        queue.enqueue('a');
        queue.enqueue('b');
        queue.enqueue('c');
        expect(queue.toArray()).toEqual(['a', 'b', 'c']);
    });

    test('dequeue removes and returns elements in FIFO order', () => {
        queue.enqueue('first');
        queue.enqueue('second');
        queue.enqueue('third');
        expect(queue.dequeue()).toBe('first');
        expect(queue.dequeue()).toBe('second');
        expect(queue.dequeue()).toBe('third');
        expect(queue.dequeue()).toBeUndefined();
    });

    test('peek returns the front element without removing it', () => {
        queue.enqueue(1);
        queue.enqueue(2);
        expect(queue.peek()).toBe(1);
        expect(queue.size()).toBe(2);
    });

    test('is empty works correctly', () => {
        expect(queue.isEmpty()).toBe(true);
        queue.enqueue(5);
        expect(queue.isEmpty()).toBe(false);
    });

    test('size returns correct number of elements', () => {
        expect(queue.size()).toBe(0);
        queue.enqueue('x');
        queue.enqueue('y');
        expect(queue.size()).toBe(2);
        queue.dequeue();
        expect(queue.size()).toBe(1);
    });

    test('dequeue on empty queue returns undefined', () => {
        expect(queue.dequeue()).toBeUndefined();
    });

    test('peek on empty queue returns undefined', () => {
        expect(queue.peek()).toBeUndefined();
    });

    test('to array fn() returns correct array representation', () => {
        queue.enqueue('alpha');
        queue.enqueue('beta');
        expect(queue.toArray()).toEqual(['alpha', 'beta']);
    });
});

"""
