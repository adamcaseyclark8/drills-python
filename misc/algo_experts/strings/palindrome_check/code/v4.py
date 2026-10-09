r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/strings/palindrome-check/code/v4.js):

function isPalindrome(string) {
    let leftIdx = 0;
    let rightIdx = string.length - 1;

    while (leftIdx < rightIdx) {
        if (string[leftIdx] !== string[rightIdx]) {
            return false;
        }
        leftIdx++;
        rightIdx--;
    }
    return true;
}

console.log(isPalindrome('hannah'));

"""
