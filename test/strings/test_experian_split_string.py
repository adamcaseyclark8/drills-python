r"""TODO: port to Python.

Original JavaScript (test/strings/experian-split-string.test.js):

const experianSplitStingFunction = require('../../code/strings/experian-split-string.js');

describe('verify experian split string function', () => {
    test('string length is 16', () => {
        expect(experianSplitStingFunction('adamcaseyclarkxx', 4)).toStrictEqual(['adam', 'case', 'ycla', 'rkxx']);
    });

    test('string length is 16', () => {
        expect(experianSplitStingFunction('adam', 4)).toStrictEqual(['adam']);
    });

    test('string length is 7', () => {
        expect(experianSplitStingFunction('adamcas', 4)).toBe('string is not divisible by 4');
    });
});

"""
