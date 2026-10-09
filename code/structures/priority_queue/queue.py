r"""TODO: port to Python.

Original JavaScript (code/structures/priority-queue/queue.js):

class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(value) {
        this.items.push(value);
    }

    dequeue() {
        return this.items.shift();
    }

    peek() {
        return this.items[0];
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }

    toArray() {
        return [...this.items];
    }
}

module.exports = Queue;

"""
