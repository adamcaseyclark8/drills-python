r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/binary-search-trees/bst-construction/code/index.js):

class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    insert(value) {
        if (value < this.value) {
            if (this.left === null) {
                this.left = new BST(value);
            } else {
                this.left.insert(value);
            }
        } else {
            if (this.right === null) {
                this.right = new BST(value);
            } else {
                this.right.insert(value);
            }
        }
        return this;
    }

    contains(value) {
        if (value < this.value) {
            if (this.left === null) {
                return false;
            } else {
                return this.left.contains(value);
            }
        } else if (value > this.value) {
            if (this.right === null) {
                return false;
            } else {
                return this.right.contains(value);
            }
        } else {
            return true;
        }
    }

    remove(value, parentNode = null) {
        let currentNode = this;

        while (currentNode !== null) {
            if (value < currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.left;
            } else if (value > currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.right;
            } else {
                if (currentNode.left !== null && currentNode.right !== null) {
                    currentNode.value = currentNode.right.getMinValue();
                    currentNode.right.remove(currentNode.value, currentNode);
                } else if (parentNode === null) {
                    if (currentNode.left !== null) {
                        currentNode.value = currentNode.left.value;
                        currentNode.right = currentNode.left.right;
                        currentNode.left = currentNode.left.left;
                    } else if (currentNode.right !== null) {
                        currentNode.value = currentNode.right.value;
                        currentNode.left = currentNode.right.right;
                        currentNode.right = currentNode.right.right;
                    } else {
                        currentNode.value = null;
                    }
                } else if (parentNode.left === currentNode) {
                    parentNode.left = currentNode.left !== null ? currentNode.left : currentNode.right;
                } else if (parentNode.right === currentNode) {
                    parentNode.right = currentNode.left !== null ? currentNode.left : currentNode.right;
                }
                break;
            }
        }
        return this;
    }

    getMinValue() {
        let currentNode = this;
        while (currentNode.left !== null) {
            currentNode = currentNode.value;
        }
    }
}

exports.BST = BST;

// replace remove value and replace it with smallest value of the right subtree
// delete the smallest value of the right subtree
//

// average: time & space O(log(n)) -> n is number of nodes
// worst: time &  O(n)
// frames on the call stack

"""
