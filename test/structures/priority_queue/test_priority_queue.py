r"""TODO: port to Python.

Original JavaScript (test/structures/priority-queue/priority-queue.test.js):

const PriorityQueue = require('../../../code/structures/priority-queue/priority-queue');

describe('testing priority queue', () => {
    let pq;

    beforeEach(() => {
        pq = new PriorityQueue();
    });

    test('enqueue and dequeue single item', () => {
        pq.enqueue('task1', 1);
        expect(pq.dequeue()).toBe('task1');
        expect(pq.isEmpty()).toBe(true);
    });

    test('items are dequeued by priority (min-priority)', () => {
        pq.enqueue('low', 5);
        pq.enqueue('medium', 3);
        pq.enqueue('high', 1);
        expect(pq.dequeue()).toBe('high');
        expect(pq.dequeue()).toBe('medium');
        expect(pq.dequeue()).toBe('low');
    });

    test('peek returns item with highest priority without removing', () => {
        pq.enqueue('A', 10);
        pq.enqueue('B', 5);
        expect(pq.peek()).toBe('B');
        expect(pq.size()).toBe(2);
    });

    test('isEmpty works correctly', () => {
        expect(pq.isEmpty()).toBe(true);
        pq.enqueue('X', 1);
        expect(pq.isEmpty()).toBe(false);
    });

    test('size reflects correct number of elements', () => {
        expect(pq.size()).toBe(0);
        pq.enqueue('task1', 2);
        pq.enqueue('task2', 3);
        expect(pq.size()).toBe(2);
        pq.dequeue();
        expect(pq.size()).toBe(1);
    });

    test('handles dequeue on empty queue gracefully', () => {
        expect(pq.dequeue()).toBeUndefined(); // or null depending on implementation
    });

    test('handles peek on empty queue gracefully', () => {
        expect(pq.peek()).toBeUndefined(); // or null depending on implementation
    });

    test('can enqueue multiple items with same priority', () => {
        pq.enqueue('A', 2);
        pq.enqueue('B', 2);
        pq.enqueue('C', 1);
        expect(pq.dequeue()).toBe('C');
        const rest = [pq.dequeue(), pq.dequeue()];
        expect(rest).toContain('A');
        expect(rest).toContain('B');
    });

    test('maintains correct ordering after interleaved operations', () => {
        pq.enqueue('task1', 4);
        pq.enqueue('task2', 2);
        expect(pq.dequeue()).toBe('task2');
        pq.enqueue('task3', 1);
        expect(pq.dequeue()).toBe('task3');
        expect(pq.dequeue()).toBe('task1');
        expect(pq.isEmpty()).toBe(true);
    });
});

"""
