r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/searching/01-binary-search/code/index-by-algo-sol-one.js):

function performBinarySearch(array, target) {
    return performBinarySearchHelper(array, target, 0, array.length - 1);
}

function performBinarySearchHelper(array, target, left, right) {
    if (left > right) {
        return -1;
    }

    const middle = Math.floor((left + right) / 2);
    const potential = array[middle];

    if (target === potential) {
        return middle;
    } else if (target > potential) {
        return performBinarySearch(array, target, left, middle - 1);
    } else {
        return performBinarySearch(array, target, middle + 1, right);
    }
}

exports.performBinarySearch = performBinarySearch;

// [1,5,23,111], 11, 0, 4
// middle: 2, potential = 5
//

"""
