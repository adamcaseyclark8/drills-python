r"""TODO: port to Python.

Original JavaScript (code/linked-lists/detect-loop-in-a-linked-list.js):

const detectLoopInALinkedList = head => {
    const set = new Set();

    while (head !== null) {
        // if this node is already present
        // in hashmap it means there is a cycle
        if (set.has(head)) return true;

        // if we are seeing the node for
        // the first time, insert it in hash
        set.add(head);

        head = head.next;
    }
    return false;
};

module.exports = detectLoopInALinkedList;

"""
