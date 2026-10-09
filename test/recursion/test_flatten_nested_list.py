r"""TODO: port to Python.

Original JavaScript (test/recursion/flatten-nested-list.test.js):

const flattenNestedList = require('../../code/recursion/flatten-nested-list.js');

describe('flattenNestedList', () => {
    describe('basic cases', () => {
        test('[1, 2, 3] → already flat, returns same values', () => {
            expect(flattenNestedList([1, 2, 3])).toEqual([1, 2, 3]);
        });

        test('[1, [2, 3]] → one level of nesting', () => {
            expect(flattenNestedList([1, [2, 3]])).toEqual([1, 2, 3]);
        });

        test('[1, [2, [3, 4]]] → two levels of nesting', () => {
            expect(flattenNestedList([1, [2, [3, 4]]])).toEqual([1, 2, 3, 4]);
        });

        test('[1, [2, [3, [4, [5]]]]] → deeply nested', () => {
            expect(flattenNestedList([1, [2, [3, [4, [5]]]]])).toEqual([1, 2, 3, 4, 5]);
        });
    });

    describe('mixed nesting', () => {
        test('[[1, 2], [3, 4], [5, 6]] → multiple nested arrays at same level', () => {
            expect(
                flattenNestedList([
                    [1, 2],
                    [3, 4],
                    [5, 6]
                ])
            ).toEqual([1, 2, 3, 4, 5, 6]);
        });

        test('[1, [2, 3], 4, [5, [6, 7]]] → mix of flat and nested', () => {
            expect(flattenNestedList([1, [2, 3], 4, [5, [6, 7]]])).toEqual([1, 2, 3, 4, 5, 6, 7]);
        });

        test('strings and numbers mixed', () => {
            expect(flattenNestedList([1, ['a', 'b'], [2, ['c']]])).toEqual([1, 'a', 'b', 2, 'c']);
        });
    });

    describe('edge cases', () => {
        test('empty array → []', () => {
            expect(flattenNestedList([])).toEqual([]);
        });

        test('array of empty arrays → []', () => {
            expect(flattenNestedList([[], [], []])).toEqual([]);
        });

        test('nested empty arrays → []', () => {
            expect(flattenNestedList([[], [[], []]])).toEqual([]);
        });

        test('single element [42] → [42]', () => {
            expect(flattenNestedList([42])).toEqual([42]);
        });

        test('does not mutate the original array', () => {
            const input = [1, [2, 3]];
            flattenNestedList(input);
            expect(input).toEqual([1, [2, 3]]);
        });
    });
});

"""
