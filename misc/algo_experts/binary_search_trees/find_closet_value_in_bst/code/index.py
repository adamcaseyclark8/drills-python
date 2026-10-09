r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/binary-search-trees/find-closet-value-in-bst/code/index.js):

function findClosestValueInBst(tree, target) {
    return findClosetValueInBstHelper(tree, target, Infinity);
}

function findClosetValueInBstHelper(tree, target, closest) {
    if (tree === null) return closest;

    if (Math.abs(target - closest) > Math.abs(target - tree.value)) {
        closest = tree.value;
    }

    if (target < tree.value) {
        return findClosetValueInBstHelper(tree.left, target, closest);
    } else if (target > tree.value) {
        return findClosetValueInBstHelper(tree.right, target, closest);
    } else {
        return closest;
    }
}

exports.findClosestValueInBst = findClosestValueInBst;

"""
