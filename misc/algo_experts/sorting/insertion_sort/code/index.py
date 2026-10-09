r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/sorting/insertion-sort/code/index.js):

function insertionSort(array) {
    for (let i = 1; i < array.length; i++) {
        let j = i;

        while (j > 0 && array[j] < array[j - 1]) {
            swap(j, j - 1, array);

            j -= 1;
        }
    }
    return array;
}

function swap(first, second, array) {
    const temp = array[second];
    array[second] = array[first];
    array[first] = temp;
}

exports.insertionSort = insertionSort;

"""
