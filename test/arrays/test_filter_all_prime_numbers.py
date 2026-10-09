r"""TODO: port to Python.

Original JavaScript (test/arrays/filter-all-prime-numbers.test.js):

const filterAllPrimeNumbers = require('../../code/arrays/filter-all-prime-numbers');

describe('filter prime numbers', () => {
    test('1 thru 100', () => {
        expect(
            filterAllPrimeNumbers([
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
            ])
        ).toEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]);
    });

    test('basic case', () => {
        expect(filterAllPrimeNumbers([1, 2, 3, 4, 5, 6, 7])).toEqual([2, 3, 5, 7]);
    });

    test('no primes', () => {
        expect(filterAllPrimeNumbers([1, 4, 6, 8, 9])).toEqual([]);
    });

    test('all primes', () => {
        expect(filterAllPrimeNumbers([2, 3, 5, 7, 11])).toEqual([2, 3, 5, 7, 11]);
    });

    test('empty array', () => {
        expect(filterAllPrimeNumbers([])).toEqual([]);
    });

    test('negative numbers', () => {
        expect(filterAllPrimeNumbers([-3, -1, 0, 1, 2])).toEqual([2]);
    });

    test('large prime', () => {
        expect(filterAllPrimeNumbers([97, 98, 99, 100])).toEqual([97]);
    });

    test('1 thru 100', () => {
        const oneThruOneHundred = [...Array(102).keys()].slice(1, -1);
        expect(filterAllPrimeNumbers(oneThruOneHundred)).toEqual([
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ]);
    });
});

"""
