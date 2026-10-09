r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/linked-lists/find-loop/code/index.js):

class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

function findLoop(head) {
    let first = head.next;
    let second = head.next.next;

    while (first !== second) {
        first = first.next;
        second = second.next.next;
    }
    first = head;

    while (first !== second) {
        first = first.next;
        second = second.next;
    }
    return first;
}

exports.LinkedList = LinkedList;
exports.findLoop = findLoop;

"""
