r"""TODO: port to Python.

Original JavaScript (code/reimplementation/assertion-utils.js):

class AssertionUtils {
    static assertEquals(expected, actual, message) {
        if (expected !== actual) {
            throw new Error(`FAIL - ${message}\n  Expected: ${expected}\n  Actual:   ${actual}`);
        }
        // console.log(`PASS - ${message}`);
    }

    static assertTrue(condition, message) {
        if (!condition) {
            throw new Error(`FAIL - ${message} | Expected: true | Actual: false`);
        }
        // console.log(`PASS - ${message}`);
    }

    static assertFalse(condition, message) {
        if (condition) {
            throw new Error(`FAIL - ${message} | Expected: false | Actual: true`);
        }
        // console.log(`PASS - ${message}`);
    }

    static assertIsNull(actual, message) {
        if (actual !== null && actual !== undefined) {
            throw new Error(`FAIL - ${message} | Expected: null | Actual: ${actual}`);
        }
        // console.log(`PASS - ${message}`);
    }

    static assertIsNotNull(actual, message) {
        if (actual === null || actual === undefined) {
            throw new Error(`FAIL - ${message} | Expected: not null | Actual: null`);
        }
        // console.log(`PASS - ${message}`);
    }

    static assertNotEquals(expected, actual, message) {
        if (expected === actual) {
            throw new Error(`FAIL - ${message} | Values should not be equal: ${expected}`);
        }
        // console.log(`PASS - ${message}`);
    }

    static assertContains(actual, substring, message) {
        if (!actual.includes(substring)) {
            throw new Error(`FAIL - ${message}\n  String: ${actual}\n  Expected to contain: ${substring}`);
        }
        // console.log(`PASS - ${message}`);
    }

    static assertArrayEquals(expected, actual, message) {
        if (expected.length !== actual.length) {
            throw new Error(`FAIL - ${message} | Array lengths differ`);
        }
        for (let i = 0; i < expected.length; i++) {
            if (expected[i] !== actual[i]) {
                throw new Error(
                    `FAIL - ${message} | Mismatch at index ${i} Expected: ${expected[i]} Actual: ${actual[i]}`
                );
            }
        }
        // console.log(`PASS - ${message}`);
    }
}

module.exports = { AssertionUtils };

"""
