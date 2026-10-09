r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/sorting/selection-sort/code/index.js):

function selectionSort(array) {
    let startIdx = 0;

    while (startIdx < array.length - 1) {
        let smallestIdx = startIdx;

        for (let i = startIdx + 1; i < array.length; i++) {
            if (array[smallestIdx] > array[i]) {
                smallestIdx = i;
            }
        }

        swap(startIdx, smallestIdx, array);
        startIdx++;
    }
    return array;
}

function swap(first, second, array) {
    const temp = array[second];
    array[second] = array[first];
    array[first] = temp;
}

exports.selectionSort = selectionSort;

"""
