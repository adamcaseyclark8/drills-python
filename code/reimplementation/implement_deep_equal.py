r"""TODO: port to Python.

Original JavaScript (code/reimplementation/implement-deep-equal.js):

const implementDeepEqualsComparison = (a, b) => {
    // 1. Strict equality check for primitive values and same object references
    if (a === b) {
        return true;
    }

    // 2. Handle null and non-object types
    if (a === null || typeof a !== 'object' || b === null || typeof b !== 'object') {
        return false;
    }

    // 3. Handle Arrays
    if (Array.isArray(a) && Array.isArray(b)) {
        if (a.length !== b.length) {
            return false;
        }
        for (let i = 0; i < a.length; i++) {
            if (!implementDeepEqualsComparison(a[i], b[i])) {
                return false;
            }
        }
        return true;
    }

    // 4. Handle Objects (non-arrays)
    if (Array.isArray(a) !== Array.isArray(b)) {
        // One is array, other is not
        return false;
    }

    const keysA = Object.keys(a);
    const keysB = Object.keys(b);

    if (keysA.length !== keysB.length) {
        return false;
    }

    for (const key of keysA) {
        if (!keysB.includes(key) || !implementDeepEqualsComparison(a[key], b[key])) {
            return false;
        }
    }

    return true;
};

module.exports = implementDeepEqualsComparison;

"""
