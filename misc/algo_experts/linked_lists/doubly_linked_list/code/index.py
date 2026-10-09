r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/linked-lists/doubly-linked-list/code/index.js):

function Node(value) {
    return {
        value: value,
        previous: null,
        next: null
    };
}

function DoublyLinkedList() {
    return {
        head: null,
        tail: null,

        setHead(node) {
            if (this.head === null) {
                this.head = node;
                this.tail = node;
                return;
            }
            this.insertBefore(this.head, node);
        },

        setTail(node) {
            if (this.tail === null) {
                this.setHead(node);
                return;
            }
            this.insertAfter(this.tail, node);
        },

        insertBefore(node, nodeToInsert) {
            if (nodeToInsert === this.head && nodeToInsert === this.tail) {
                return;
            }

            this.remove(nodeToInsert);
            nodeToInsert.previous = node.previous;
            nodeToInsert.next = node;

            if (node.previous === null) {
                this.head = nodeToInsert;
            } else {
                node.previous.next = nodeToInsert;
            }
            node.previous = nodeToInsert;
        },

        insertAfter(node, nodeToInsert) {
            if (nodeToInsert === this.head && nodeToInsert === this.tail) {
                return;
            }

            this.remove(nodeToInsert);
            nodeToInsert.previous = node;
            nodeToInsert.next = node.next;

            if (node.next === null) {
                this.tail = nodeToInsert;
            } else {
                node.next.previous = nodeToInsert;
            }
            node.next = nodeToInsert;
        },

        insertAtPosition(position, nodeToInsert) {
            if (position === 1) {
                this.setHead(nodeToInsert);
                return;
            }

            let node = this.head;
            let currentPosition = 1;
            while (node !== null && currentPosition++ !== position) {
                node = node.next;

                if (node !== null) {
                    this.insertBefore(node, nodeToInsert);
                } else {
                    this.setTail(nodeToInsert);
                }
            }
        },

        removeNodesWithValue(value) {
            let node = this.head;
            while (node !== null) {
                const nodeToRemove = node;
                node = node.next;
                if (nodeToRemove.value === value) {
                    this.remove(nodeToRemove);
                }
            }
        },

        containsNodeWithValue(value) {
            let node = this.head;
            while (node !== null && node.value !== value) {
                node = node.next;
            }
            return node !== null;
        },

        remove(node) {
            if (node === this.head) {
                this.head = this.head.next;
            }

            if (node === this.tail) {
                this.tail = this.tail.previous;
            }

            this.removeNodeBindings(node);
        },

        removeNodeBindings(node) {
            if (node.previous !== null) {
                node.previous.next = node.next;
            }

            if (node.next !== null) {
                node.next.previous = node.previous;
            }

            node.previous = null;
            node.next = null;
        }
    };
}

exports.Node = Node;
exports.DoublyLinkedList = DoublyLinkedList;

"""
