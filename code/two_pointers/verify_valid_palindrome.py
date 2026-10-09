r"""TODO: port to Python.

Original JavaScript (code/two-pointers/verify-valid-palindrome.js):

const verifyValidPalindrome = s => {
    // Clean the string: remove non-alphanumeric chars and lowercase
    if (s.length === 0 || !s) {
        return false;
    }

    const cleaned = s.replace(/[^0-9a-zA-Z]/g, '').toLowerCase();

    let left = 0;
    let right = cleaned.length - 1;

    while (left < right) {
        if (cleaned[left] !== cleaned[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
};

module.exports = verifyValidPalindrome;

"""
