r"""TODO: port to Python.

Original JavaScript (test/arrays/merge-array-intervals.test.js):

const mergeArrayIntervals = require('../../code/arrays/merge-array-intervals');

// EACH INTERVAL HAS EXACTLY 2 ELEMENTS [START, END]
// START <= END ALWAYS (A VALID INTERVAL NEVER GOES BACKWARDS)
// INTERVALS CAN OVERLAP, TOUCH, OR BE COMPLETELY NESTED
// INPUT CAN BE UNSORTED
// VALUES CAN BE NEGATIVE
// ARRAY CAN BE EMPTY

describe('merge array intervals tests ', () => {
    test('basic overlapping intervals', () => {
        expect(
            mergeArrayIntervals([
                [1, 3],
                [2, 6],
                [8, 10],
                [15, 18]
            ])
        ).toEqual([
            [1, 6],
            [8, 10],
            [15, 18]
        ]);
    });

    test('intervals that touch at boundary', () => {
        expect(
            mergeArrayIntervals([
                [1, 4],
                [4, 5]
            ])
        ).toEqual([[1, 5]]);
    });

    test('no overlapping intervals', () => {
        expect(
            mergeArrayIntervals([
                [1, 2],
                [3, 4],
                [5, 6]
            ])
        ).toEqual([
            [1, 2],
            [3, 4],
            [5, 6]
        ]);
    });

    test('all intervals merge into one', () => {
        expect(
            mergeArrayIntervals([
                [1, 4],
                [2, 5],
                [3, 6]
            ])
        ).toEqual([[1, 6]]);
    });

    test('one interval completely contains another', () => {
        expect(
            mergeArrayIntervals([
                [1, 10],
                [2, 5]
            ])
        ).toEqual([[1, 10]]);
    });

    test('unsorted input', () => {
        expect(
            mergeArrayIntervals([
                [8, 10],
                [1, 3],
                [2, 6],
                [15, 18]
            ])
        ).toEqual([
            [1, 6],
            [8, 10],
            [15, 18]
        ]);
    });

    test('single interval', () => {
        expect(mergeArrayIntervals([[1, 5]])).toEqual([[1, 5]]);
    });

    test('two non-overlapping intervals', () => {
        expect(
            mergeArrayIntervals([
                [1, 2],
                [4, 5]
            ])
        ).toEqual([
            [1, 2],
            [4, 5]
        ]);
    });
});

"""
