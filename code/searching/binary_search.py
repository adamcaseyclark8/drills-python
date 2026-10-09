r"""TODO: port to Python.

Original JavaScript (code/searching/binary-search.js):

const performBinarySearch = (array, number) => {
    const search = (numbers, target, left, right) => {
        if (left > right) {
            return -1;
        }

        const middle = Math.floor((left + right) / 2);
        const potential = array[middle];

        if (target === potential) {
            return middle;
        } else if (target > potential) {
            return search(numbers, target, middle + 1, right);
        } else {
            return search(numbers, target, left, middle - 1);
        }
    };

    return search(array, number, 0, array.length - 1);
};

module.exports = performBinarySearch;

"""
