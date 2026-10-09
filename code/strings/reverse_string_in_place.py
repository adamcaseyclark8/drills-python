r"""TODO: port to Python.

Original JavaScript (code/strings/reverse-string-in-place.js):

// Function to reverse string in place using two-pointer technique
const reverseStringInPlace = str => {
    // Convert string to array to mutate it
    let charArray = str.split('');
    let left = 0;
    let right = charArray.length - 1;

    // Swap characters until the pointers meet in the middle
    while (left < right) {
        // Swap characters at left and right pointers
        [charArray[left], charArray[right]] = [charArray[right], charArray[left]];
        // Move the pointers towards the middle
        left++;
        right--;
    }

    // Convert array back to string
    return charArray.join('');
};

module.exports = reverseStringInPlace;

"""
