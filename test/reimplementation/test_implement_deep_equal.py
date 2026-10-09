r"""TODO: port to Python.

Original JavaScript (test/reimplementation/implement-deep-equal.test.js):

const implementDeepEqualsComparison = require('../../code/reimplementation/implement-deep-equal.js');

describe('verify implement deep equals function', () => {
    test('compare two of the same numbers', () => {
        expect(implementDeepEqualsComparison(5, 5)).toBe(true);
    });

    test('compare two different numbers', () => {
        expect(implementDeepEqualsComparison(5, 10)).toBe(false);
    });

    test('compare two of the same strings', () => {
        expect(implementDeepEqualsComparison('hello', 'hello')).toBe(true);
    });

    test('compare two different strings', () => {
        expect(implementDeepEqualsComparison('hello', 'world')).toBe(false);
    });

    test('compare the same booleans', () => {
        expect(implementDeepEqualsComparison(true, true)).toBe(true);
    });

    test('compare different booleans', () => {
        expect(implementDeepEqualsComparison(true, false)).toBe(false);
    });

    // test('compare NaN with Nan', () => {
    //     expect(implementDeepEqualsComparison(NaN, NaN)).toBe(true)
    // });

    test('comparing null values', () => {
        expect(implementDeepEqualsComparison(null, null)).toBe(true);
    });

    test('comparing null with not null values', () => {
        expect(implementDeepEqualsComparison(null, 'hello')).toBe(false);
        expect(implementDeepEqualsComparison(null, 3)).toBe(false);
        expect(implementDeepEqualsComparison(null, true)).toBe(false);
    });

    test('compare identical arrays', () => {
        expect(implementDeepEqualsComparison([1, 2, 3], [1, 2, 3])).toBe(true);
    });

    test('compare different lengths arrays', () => {
        expect(implementDeepEqualsComparison([1, 2, 3], [1, 2])).toBe(false);
    });

    test('compare same length arrays with diff values', () => {
        expect(implementDeepEqualsComparison([1, 2, 3], [1, 2, 4])).toBe(false);
    });

    // test('compare arrays of same elements, different order', () => {
    //     expect(implementDeepEqualsComparison([1, 2, 3], [3, 2, 1])).toBe(true);
    // });

    test('compare nested arrays', () => {
        const firstNestedArrays = [
            [
                [1, 2],
                [3, 4]
            ],
            [5, 6],
            [7, 8]
        ];
        const secondNestedArrays = [
            [
                [1, 2],
                [3, 4]
            ],
            [5, 6],
            [7, 8]
        ];

        expect(implementDeepEqualsComparison(firstNestedArrays, secondNestedArrays)).toBe(true);
    });

    test('compare 2 identical objects', () => {
        expect(implementDeepEqualsComparison({ a: 1, b: 2 }, { a: 1, b: 2 })).toBe(true);
    });
});

"""
