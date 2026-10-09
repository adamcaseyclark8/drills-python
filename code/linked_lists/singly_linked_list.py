r"""TODO: port to Python.

Original JavaScript (code/linked-lists/singly-linked-list.js):

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class List {
    constructor() {
        this.head = null;
        this.length = 0;
    }

    push(value) {
        const node = new Node(value);
        if (!this.head) {
            this.head = node;
        } else {
            let current = this.head;
            while (current.next) current = current.next;
            current.next = node;
        }
        this.length++;
        return node;
    }

    pop() {
        if (!this.head) return null;

        if (!this.head.next) {
            const node = this.head;
            this.head = null;
            this.length--;
            return node;
        }

        let current = this.head;
        while (current.next.next) current = current.next;
        const node = current.next;
        current.next = null;
        this.length--;
        return node;
    }

    delete(value) {
        if (!this.head) return null;

        if (this.head.value === value) {
            const node = this.head;
            this.head = this.head.next;
            this.length--;
            return node;
        }

        let current = this.head;
        while (current.next && current.next.value !== value) {
            current = current.next;
        }

        if (current.next) {
            const node = current.next;
            current.next = current.next.next;
            this.length--;
            return node;
        }

        return null; // value not found
    }

    find(value) {
        let current = this.head;
        while (current) {
            if (current.value === value) return current;
            current = current.next;
        }
        return null;
    }

    toArray() {
        const arr = [];
        let current = this.head;
        while (current) {
            arr.push(current.value);
            current = current.next;
        }
        return arr;
    }
}

module.exports = { Node, List };

"""
