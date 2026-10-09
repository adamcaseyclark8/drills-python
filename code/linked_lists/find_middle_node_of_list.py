r"""TODO: port to Python.

Original JavaScript (code/linked-lists/find-middle-node-of-list.js):

class ListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

// helper to build a linked list from an array
const buildList = arr => {
    if (!arr.length) return null;
    const head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
};

// helper to convert a linked list back to an array (for easy test assertions)
const listToArray = head => {
    const result = [];
    let current = head;
    while (current) {
        result.push(current.val);
        current = current.next;
    }
    return result;
};

// slow/fast pointer technique — when fast reaches the end, slow is at the middle
const findMiddleNode = head => {
    let slow = head;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
};

module.exports = { findMiddleNode, buildList, listToArray };

"""
