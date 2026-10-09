r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/sorting/quick-sort/test/index.test.js):

const { quickSort } = require('../code/index');

describe('Quick sort', () => {
    test('test case #01', () => {
        const array = [1];
        expect(quickSort(array)).toStrictEqual([1]);
    });

    test('test case #02', () => {
        const array = [1, 2];
        expect(quickSort(array)).toStrictEqual([1, 2]);
    });

    test('test case #03', () => {
        const array = [2, 1];
        expect(quickSort(array)).toStrictEqual([1, 2]);
    });

    test('test case #04', () => {
        const array = [1, 3, 2];
        expect(quickSort(array)).toStrictEqual([1, 2, 3]);
    });

    test('test case #05', () => {
        const array = [3, 1, 2];
        expect(quickSort(array)).toStrictEqual([1, 2, 3]);
    });

    test('test case #06', () => {
        const array = [1, 2, 3];
        expect(quickSort(array)).toStrictEqual([1, 2, 3]);
    });

    test('test case #07', () => {
        const array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8];
        expect(quickSort(array)).toStrictEqual([
            -10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10
        ]);
    });

    test('test case #08', () => {
        const array = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8];
        expect(quickSort(array)).toStrictEqual([-10, -10, -9, -7, -7, -6, -5, -2, 2, 2, 3, 3, 4, 5, 8, 8, 9, 10]);
    });

    test('test case #09', () => {
        const array = [8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4];
        expect(quickSort(array)).toStrictEqual([
            -10, -10, -9, -6, -5, -2, -2, -1, 1, 2, 4, 4, 6, 7, 7, 8, 8, 8, 8, 9, 10, 10
        ]);
    });

    test('test case #10', () => {
        const array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1];
        expect(quickSort(array)).toStrictEqual([-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]);
    });

    test('test case #11', () => {
        const array = [
            2, -2, -6, -10, 10, 4, -8, -1, -8, -4, 7, -4, 0, 9, -9, 0, -9, -9, 8, 1, -4, 4, 8, 5, 1, 5, 0, 0, 2, -10
        ];
        expect(quickSort(array)).toStrictEqual([
            -10, -10, -9, -9, -9, -8, -8, -6, -4, -4, -4, -2, -1, 0, 0, 0, 0, 1, 1, 2, 2, 4, 4, 5, 5, 7, 8, 8, 9, 10
        ]);
    });

    test('test case #12', () => {
        const array = [4, 1, 5, 0, -9, -3, -3, 9, 3, -4, -9, 8, 1, -3, -7, -4, -9, -1, -7, -2, -7, 4];
        expect(quickSort(array)).toStrictEqual([
            -9, -9, -9, -7, -7, -7, -4, -4, -3, -3, -3, -2, -1, 0, 1, 1, 3, 4, 4, 5, 8, 9
        ]);
    });

    test('test case #13', () => {
        const array = [
            427, 787, 222, 996, -359, -614, 246, 230, 107, -706, 568, 9, -246, 12, -764, -212, -484, 603, 934, -848,
            -646, -991, 661, -32, -348, -474, -439, -56, 507, 736, 635, -171, -215, 564, -710, 710, 565, 892, 970, -755,
            55, 821, -3, -153, 240, -160, -610, -583, -27, 131
        ];
        expect(quickSort(array)).toStrictEqual([
            -991, -848, -764, -755, -710, -706, -646, -614, -610, -583, -484, -474, -439, -359, -348, -246, -215, -212,
            -171, -160, -153, -56, -32, -27, -3, 9, 12, 55, 107, 131, 222, 230, 240, 246, 427, 507, 564, 565, 568, 603,
            635, 661, 710, 736, 787, 821, 892, 934, 970, 996
        ]);
    });

    // test("test case #14", () => {
    //   const array = [
    //     991,
    //     731,
    //     882,
    //     100,
    //     280,
    //     43,
    //     432,
    //     771,
    //     581,
    //     180,
    //     382,
    //     998,
    //     847,
    //     80,
    //     220,
    //     680,
    //     769,
    //     85,
    //     817,
    //     366,
    //     956,
    //     749,
    //     471,
    //     228,
    //     435,
    //     269,
    //     652,
    //     331,
    //     387,
    //     657,
    //     255,
    //     382,
    //     216,
    //     6,
    //     163,
    //     681,
    //     80,
    //     913,
    //     169,
    //     972,
    //     523,
    //     354,
    //     747,
    //     805,
    //     382,
    //     827,
    //     796,
    //     372,
    //     753,
    //     519,
    //     906
    //   ];
    //   expect(quickSort(array)).toStrictEqual([998,882,827,817,796,731]);
    // });
    //
    // test("test case #15", () => {
    //   const array = [];
    //   expect(quickSort(array)).toStrictEqual([]));
    // });
    //
    // test("test case #16", () => {
    //   const array = [];
    //   expect(quickSort(array)).toStrictEqual([]));
    // });
    //
    // test("test case #17", () => {
    //   const array = [];
    //   expect(quickSort(array)).toStrictEqual([]));
    // });
    //
    // test("test case #18", () => {
    //   const array = [];
    //   expect(quickSort(array)).toStrictEqual([]));
    // });
});

"""
