r"""TODO: port to Python.

Original JavaScript (test/sorting/merge-overlapping-arrays.test.js):

const mergeOverlappingArrays = require('../../code/sorting/merge-overlapping-arrays.js');

describe('verify merge overlapping array', () => {
    test('one overlapping scenario', () => {
        expect(
            mergeOverlappingArrays([
                [1, 3],
                [2, 6],
                [8, 10],
                [15, 18]
            ])
        ).toStrictEqual([
            [1, 6],
            [8, 10],
            [15, 18]
        ]);
    });

    test('two overlapping scenarios', () => {
        expect(
            mergeOverlappingArrays([
                [1, 4],
                [2, 5],
                [3, 6],
                [7, 9]
            ])
        ).toStrictEqual([
            [1, 6],
            [7, 9]
        ]);
    });

    test('duplicated start and finish', () => {
        expect(
            mergeOverlappingArrays([
                [1, 3],
                [5, 5],
                [2, 6],
                [7, 9]
            ])
        ).toStrictEqual([
            [1, 6],
            [7, 9]
        ]);
    });

    test('duplicated duplicated start and finish', () => {
        expect(
            mergeOverlappingArrays([
                [1, 3],
                [5, 5],
                [5, 5],
                [2, 6],
                [7, 9]
            ])
        ).toStrictEqual([
            [1, 6],
            [7, 9]
        ]);
    });

    test('another with no overlaps', () => {
        expect(
            mergeOverlappingArrays([
                [1, 3],
                [5, 5]
            ])
        ).toStrictEqual([
            [1, 3],
            [5, 5]
        ]);
    });

    test('no overlapping arrays', () => {
        expect(
            mergeOverlappingArrays([
                [1, 3],
                [4, 6],
                [7, 9],
                [10, 11]
            ])
        ).toStrictEqual([
            [1, 3],
            [4, 6],
            [7, 9],
            [10, 11]
        ]);
    });

    test('empty array', () => {
        expect(mergeOverlappingArrays([])).toStrictEqual([]);
    });

    test('single nested array', () => {
        expect(mergeOverlappingArrays([1, 2])).toStrictEqual([1, 2]);
    });
});

"""
