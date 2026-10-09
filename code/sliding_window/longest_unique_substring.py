r"""TODO: port to Python.

Original JavaScript (code/sliding-window/longest-unique-substring.js):

const longestUniqueSubstring = string => {
    const seen = new Set();
    let left = 0;
    let longest = '';

    for (let right = 0; right < string.length; right++) {
        while (seen.has(string[right])) {
            seen.delete(string[left]);
            left++;
        }
        seen.add(string[right]);
        if (right - left + 1 > longest.length) {
            longest = string.slice(left, right + 1);
        }
    }
    return longest;
};

module.exports = longestUniqueSubstring;

"""
