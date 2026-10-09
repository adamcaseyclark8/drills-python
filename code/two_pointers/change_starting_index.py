r"""TODO: port to Python.

Original JavaScript (code/two-pointers/change-starting-index.js):

const changeStartingIndex = (numbers, change) => {
    if (!Number.isInteger(change) || change < 0) {
        throw new Error('change must be an positive integer');
    }

    if (change === 0) {
        return numbers;
    }

    if (numbers.length === 0) {
        return [];
    }

    const first = 0;
    const last = numbers.length - 1;
    const leftAdjustedIndex = numbers.length - change;
    const newStartLocation = leftAdjustedIndex % numbers.length;
    const newEndLocation = newStartLocation - 1;

    // console.log(
    //     'first =>', first,
    //     'last =>', last,
    //     'leftAdjustedIndex =>', leftAdjustedIndex,
    //     'newStartLocation =>', newStartLocation,
    //     'newEndLocation =>', newEndLocation
    // )

    const reverseArrayInPlace = (start, end, array) => {
        while (start < end) {
            [array[start], array[end]] = [array[end], array[start]];
            start++;
            end--;
        }
        return array;
    };

    // entire array, beginning to new end location, new start to end
    reverseArrayInPlace(0, numbers.length - 1, numbers);
    reverseArrayInPlace(0, newEndLocation, numbers);
    reverseArrayInPlace(newStartLocation, last, numbers);

    return numbers;
};

module.exports = changeStartingIndex;

// console.log(changeStartingIndex([1,2,3,4,5,6,7,8,9,10], 3))

"""
