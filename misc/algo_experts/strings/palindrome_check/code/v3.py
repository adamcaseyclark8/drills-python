r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/strings/palindrome-check/code/v3.js):

function isPalindrome(string, i = 0) {
    const j = string.length - 1 - i;
    return i >= j ? true : string[i] === string[j] && isPalindrome(string, i + 1);
}

exports.isPalindrome = isPalindrome;

console.log(isPalindrome('hannah'));

"""
