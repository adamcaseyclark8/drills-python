r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/famous-algorithms/01-kadanes/test/index.test.js):

const { Kadanes } = require('../code/index-by-algo');

describe('', () => {
    test('test case 1', () => {
        const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        expect(Kadanes(array)).toStrictEqual(55);
    });

    test('test case 2', () => {
        const array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10];
        expect(Kadanes(array)).toStrictEqual(-1);
    });

    test('test case 3', () => {
        const array = [-10, -2, -9, -4, -8, -6, -7, -1, -5];
        expect(Kadanes(array)).toStrictEqual(-1);
    });

    test('test case 4', () => {
        const array = [1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10];
        expect(Kadanes(array)).toStrictEqual(35);
    });

    // test("test case 5", () => {
    //   expect(Kadanes()).toStrictEqual(34);
    // });
    //
    // test("test case 6", () => {
    //   expect(Kadanes()).toStrictEqual(11);
    // });
    //
    // test("test case 7", () => {
    //   expect(Kadanes()).toStrictEqual(16);
    // });
    //
    // test("test case 8", () => {
    //   expect(Kadanes()).toStrictEqual(19);
    // });
    //
    // test("test case 9", () => {
    //   expect(kadanes()).toStrictEqual(23);
    // });
    //
    // test("test case 10", () => {
    //   expect(kadanes()).toStrictEqual(24);
    // });
    //
    // test("test case 11", () => {
    //   expect(kadanes()).toStrictEqual(22);
    // });
    //
    // test("test case 12", () => {
    //   expect(kadanes()).toStrictEqual(35);
    // });
    //
    // test("test case 13", () => {
    //   expect(kadanes()).toStrictEqual(135);
    // });
});

"""
