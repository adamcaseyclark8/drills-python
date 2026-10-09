r"""TODO: port to Python.

Original JavaScript (code/sorting/bubble-sort.js):

// AS EVERY COUNTER++,

const sortViaBubbleSort = array => {
    let isSorted = false;
    let counter = 0;

    while (!isSorted) {
        isSorted = true;

        for (let i = 0; i < array.length - 1 - counter; i++) {
            if (array[i] > array[i + 1]) {
                swap(i, i + 1, array);
                isSorted = false;
            }
        }
        counter++;
    }
    return array;
};

function swap(first, second, array) {
    const temp = array[second];
    array[second] = array[first];
    array[first] = temp;
}

module.exports = sortViaBubbleSort;

"""
