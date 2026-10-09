r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/searching/01-binary-search/code/index-by-algo-sol-two.js):

function performBinarySearch(array, target) {
    return performBinarySearchHelper(array, target, 0, array.length - 1);
}

function performBinarySearchHelper(array, target, left, right) {
    // loop through array

    while (left <= right) {
        const middle = Math.floor((left + right) / 2);
        const potential = array[middle];

        console.log(`middle: ${middle}, target: ${target} vs. potential: ${potential}, left: ${left}, right: ${right}`);

        if (target === potential) {
            return middle;
        } else if (target < potential) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return -1;
}

exports.performBinarySearch = performBinarySearch;

"""
