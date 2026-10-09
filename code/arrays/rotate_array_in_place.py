r"""TODO: port to Python.

Original JavaScript (code/arrays/rotate-array-in-place.js):

const rotateArrayInPlace = (numbers, change) => {
    let k = change % numbers.length;

    if (!Number.isInteger(change) || change < 0) {
        throw new Error('change must be an positive integer');
    }

    if (change === 0) {
        return numbers;
    }

    if (numbers.length === 0) {
        return [];
    }

    const reverse = (left, right, array) => {
        while (left < right) {
            [array[left], array[right]] = [array[right], array[left]];
            left++;
            right--;
        }
    };

    // console.log(
    //     'first =>', 0,
    //     'last =>', numbers.length - 1,
    //     'leftAdjustedIndex =>', change % numbers.length,
    //     'newStartLocation =>', k,
    //     'newEndLocation =>', k - 1
    // )

    reverse(0, numbers.length - 1, numbers);
    reverse(0, k - 1, numbers);
    reverse(k, numbers.length - 1, numbers);

    return numbers;
};

module.exports = rotateArrayInPlace;

// console.log(rotateArrayInPlace([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 3))

"""
