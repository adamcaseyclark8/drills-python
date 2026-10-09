r"""TODO: port to Python.

Original JavaScript (code/structures/implement-stack-using-queues.js):

class StackUsingQueues {
    constructor() {
        this.queue1 = [];
        this.queue2 = [];
    }

    // push: enqueue to queue1, then rotate so newest element is always at the front
    push(val) {
        this.queue2.push(val);
        while (this.queue1.length) {
            this.queue2.push(this.queue1.shift());
        }
        [this.queue1, this.queue2] = [this.queue2, this.queue1];
    }

    // pop: dequeue from the front of queue1 (which holds the top of stack)
    pop() {
        if (this.isEmpty()) return null;
        return this.queue1.shift();
    }

    // peek: look at the front of queue1 without removing
    peek() {
        if (this.isEmpty()) return null;
        return this.queue1[0];
    }

    isEmpty() {
        return this.queue1.length === 0;
    }

    size() {
        return this.queue1.length;
    }
}

module.exports = StackUsingQueues;

"""
