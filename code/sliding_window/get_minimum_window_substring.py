r"""TODO: port to Python.

Original JavaScript (code/sliding-window/get-minimum-window-substring.js):

const getMinimumWindowSubstring = (s, t) => {
    if (!s || !t) return '';

    const need = new Map();
    for (const c of t) need.set(c, (need.get(c) || 0) + 1);

    let left = 0;
    let formed = 0;
    let minLen = Infinity;
    let minStart = 0;
    const window = new Map();

    for (let right = 0; right < s.length; right++) {
        const c = s[right];
        window.set(c, (window.get(c) || 0) + 1);

        if (need.has(c) && window.get(c) === need.get(c)) formed++;

        while (formed === need.size) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }

            const leftChar = s[left];
            window.set(leftChar, window.get(leftChar) - 1);
            if (need.has(leftChar) && window.get(leftChar) < need.get(leftChar)) formed--;
            left++;
        }
    }

    return minLen === Infinity ? '' : s.substring(minStart, minStart + minLen);
};

module.exports = getMinimumWindowSubstring;

"""
