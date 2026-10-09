r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/searching/01-binary-search/test/index.test.js):

// const { performBinarySearch } = require("./index.js");
// const { performBinarySearch } = require("../code/index-by-algo-sol-one.js");
const { performBinarySearch } = require('../code/index-by-algo-sol-two.js');

describe('Binary Search', () => {
    // test("test case #1", () => {
    //   const array = [1, 5, 23, 111];
    //   expect(performBinarySearch(array, 111)).toStrictEqual(3);
    // });
    //
    // test("test case #2", () => {
    //   const array = [1, 5, 23, 111];
    //   expect(performBinarySearch(array, 5)).toStrictEqual(1);
    // });
    //
    // test("test case #3", () => {
    //   const array = [1, 5, 23, 111];
    //   expect(performBinarySearch(array, 35)).toStrictEqual(-1);
    // });
    //
    // test("test case #4", () => {
    //   const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73];
    //   expect(performBinarySearch(array, 33)).toStrictEqual(3);
    // });
    //
    // test("test case #5", () => {
    //   const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73];
    //   expect(performBinarySearch(array, 72)).toStrictEqual(8);
    // });
    //
    // test("test case #6", () => {
    //   const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73];
    //   expect(performBinarySearch(array, 73)).toStrictEqual(9);
    // });

    test('test case #7', () => {
        const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73];
        expect(performBinarySearch(array, 70)).toStrictEqual(-1);
    });

    // test("test case #8", () => {
    //   const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355];
    //   expect(performBinarySearch(array, 355)).toStrictEqual(10);
    // });
    //
    // test("test case #9", () => {
    //   const array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 354];
    //   expect(performBinarySearch(array, 355)).toStrictEqual(-1);
    // });
});

"""
