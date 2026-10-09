r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/arrays/move-element-to-end/code/move-element-to-end.js):

function moveElementToEnd(array) {
    let count = 0;
    for (const num of array) {
        if (num === 0) {
            array[count] = array[count + 1];
            array[count] = array[count + 1];
            count++;
        }
    }
    return array;
}

exports.moveElementToEnd = moveElementToEnd;

"""
