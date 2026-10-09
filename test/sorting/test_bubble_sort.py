r"""TODO: port to Python.

Original JavaScript (test/sorting/bubble-sort.test.js):

const sortViaBubbleSort = require('../../code/sorting/bubble-sort.js');

describe('verify bubble sorting function', () => {
    test('I', () => {
        expect(sortViaBubbleSort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1])).toStrictEqual([
            -10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9
        ]);
    });

    test('II', () => {
        const array = [1, 2];
        expect(sortViaBubbleSort(array)).toStrictEqual([1, 2]);
    });

    test('III', () => {
        const array = [2, 1];
        expect(sortViaBubbleSort(array)).toStrictEqual([1, 2]);
    });

    test('IV', () => {
        const array = [1, 3, 2];
        expect(sortViaBubbleSort(array)).toStrictEqual([1, 2, 3]);
    });

    test('V', () => {
        const array = [3, 1, 2];
        expect(sortViaBubbleSort(array)).toStrictEqual([1, 2, 3]);
    });

    test('VI', () => {
        const array = [1, 2, 3];
        expect(sortViaBubbleSort(array)).toStrictEqual([1, 2, 3]);
    });

    test('VII', () => {
        const array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8];
        expect(sortViaBubbleSort(array)).toStrictEqual([
            -10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10
        ]);
    });

    test('VIII', () => {
        const array = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8];
        expect(sortViaBubbleSort(array)).toStrictEqual([
            -10, -10, -9, -7, -7, -6, -5, -2, 2, 2, 3, 3, 4, 5, 8, 8, 9, 10
        ]);
    });

    test('IX', () => {
        const array = [8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4];
        expect(sortViaBubbleSort(array)).toStrictEqual([
            -10, -10, -9, -6, -5, -2, -2, -1, 1, 2, 4, 4, 6, 7, 7, 8, 8, 8, 8, 9, 10, 10
        ]);
    });

    test('X', () => {
        const array = [1];
        expect(sortViaBubbleSort(array)).toStrictEqual([1]);
    });

    test('XI', () => {
        const array = [
            2, -2, -6, -10, 10, 4, -8, -1, -8, -4, 7, -4, 0, 9, -9, 0, -9, -9, 8, 1, -4, 4, 8, 5, 1, 5, 0, 0, 2, -10
        ];
        expect(sortViaBubbleSort(array)).toStrictEqual([
            -10, -10, -9, -9, -9, -8, -8, -6, -4, -4, -4, -2, -1, 0, 0, 0, 0, 1, 1, 2, 2, 4, 4, 5, 5, 7, 8, 8, 9, 10
        ]);
    });

    test('XII', () => {
        const array = [4, 1, 5, 0, -9, -3, -3, 9, 3, -4, -9, 8, 1, -3, -7, -4, -9, -1, -7, -2, -7, 4];
        expect(sortViaBubbleSort(array)).toStrictEqual([
            -9, -9, -9, -7, -7, -7, -4, -4, -3, -3, -3, -2, -1, 0, 1, 1, 3, 4, 4, 5, 8, 9
        ]);
    });

    test('XIII', () => {
        const array = [
            427, 787, 222, 996, -359, -614, 246, 230, 107, -706, 568, 9, -246, 12, -764, -212, -484, 603, 934, -848,
            -646, -991, 661, -32, -348, -474, -439, -56, 507, 736, 635, -171, -215, 564, -710, 710, 565, 892, 970, -755,
            55, 821, -3, -153, 240, -160, -610, -583, -27, 131
        ];
        expect(sortViaBubbleSort(array)).toStrictEqual([
            -991, -848, -764, -755, -710, -706, -646, -614, -610, -583, -484, -474, -439, -359, -348, -246, -215, -212,
            -171, -160, -153, -56, -32, -27, -3, 9, 12, 55, 107, 131, 222, 230, 240, 246, 427, 507, 564, 565, 568, 603,
            635, 661, 710, 736, 787, 821, 892, 934, 970, 996
        ]);
    });
});

"""
