r"""TODO: port to Python.

Original JavaScript (code/sorting/bubble-sort/code/v2.js):

function sortViaBubbleSort(array) {
    let swapped = false;
    let count = 0;

    console.log(count);

    do {
        swapped = false;

        array.forEach((item, index) => {
            count++;

            if (item > array[index + 1]) {
                const temporary = item;

                array[index] = array[index + 1];
                array[index + 1] = temporary;

                swapped = true;
            }
        });
    } while (swapped);

    return array;
}

module.exports = sortViaBubbleSort;

"""
