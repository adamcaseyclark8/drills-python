r"""TODO: port to Python.

Original JavaScript (test/hashing/longest-sequence-of-numbers.test.js):

const longestSequenceOfNumbers = require('../../code/hashing/longest-sequence-of-numbers.js');

describe('verify longest sequence of numbers', () => {
    test('has duplicated numbers', () => {
        expect(longestSequenceOfNumbers([100, 4, 4, 200, 1, 3, 2])).toBe(4);
    });

    test('handles large number of duplicates efficiently', () => {
        // THIS TEST WILL FAIL IF SET IS NOT USED

        const arrayOfNumbers = new Array(50000).fill(1).concat([2, 3, 4]);

        const start = Date.now();
        const results = longestSequenceOfNumbers(arrayOfNumbers);
        const elapsed = Date.now() - start;

        expect(results).toBe(4);
        expect(elapsed).toBeLessThan(100);
    });

    test('size 4 sequence', () => {
        expect(longestSequenceOfNumbers([100, 4, 200, 1, 3, 2])).toBe(4);
    });

    test('3 separate sequences of 2', () => {
        expect(longestSequenceOfNumbers([200, 199, 100, 99, 3, 2])).toBe(2);
    });

    test('empty array', () => {
        expect(longestSequenceOfNumbers([])).toBe(0);
    });

    test('one number sequence', () => {
        expect(longestSequenceOfNumbers([4])).toBe(1);
    });

    test('two number sequence', () => {
        expect(longestSequenceOfNumbers([1, 2])).toBe(2);
    });

    test('size 5 sequence', () => {
        expect(longestSequenceOfNumbers([100, 5, 4, 200, 1, 3, 2])).toBe(5);
    });
});

"""
