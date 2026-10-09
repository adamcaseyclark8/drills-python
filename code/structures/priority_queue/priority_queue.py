r"""TODO: port to Python.

Original JavaScript (code/structures/priority-queue/priority-queue.js):

const Queue = require('./queue.js');

class PriorityQueue extends Queue {
    constructor() {
        super();
    }

    enqueue(value, priority) {
        const newItem = { value, priority };

        if (this.isEmpty()) {
            this.items.push(newItem);
        } else {
            let inserted = false;
            for (let i = 0; i < this.items.length; i++) {
                if (priority < this.items[i].priority) {
                    this.items.splice(i, 0, newItem);
                    inserted = true;
                    break;
                }
            }
            if (!inserted) {
                this.items.push(newItem);
            }
        }
    }

    dequeue() {
        const item = super.dequeue();
        return item?.value;
    }

    peek() {
        return super.peek()?.value;
    }

    toArray() {
        return this.items.map(item => item.value);
    }
}

module.exports = PriorityQueue;

"""
