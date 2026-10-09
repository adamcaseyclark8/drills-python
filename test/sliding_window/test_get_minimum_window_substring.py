r"""TODO: port to Python.

Original JavaScript (test/sliding-window/get-minimum-window-substring.test.js):

const getMinimumWindowSubstring = require('../../code/sliding-window/get-minimum-window-substring.js');

describe('getMinimumWindowSubstring', () => {
    test('ADOBECODEBANC and ABC returns BANC', () => {
        expect(getMinimumWindowSubstring('ADOBECODEBANC', 'ABC')).toBe('BANC');
    });

    test('a and a returns a', () => {
        expect(getMinimumWindowSubstring('a', 'a')).toBe('a');
    });

    test('a and b returns empty string', () => {
        expect(getMinimumWindowSubstring('a', 'b')).toBe('');
    });

    test('empty s returns empty string', () => {
        expect(getMinimumWindowSubstring('', 'a')).toBe('');
    });

    test('empty t returns empty string', () => {
        expect(getMinimumWindowSubstring('abc', '')).toBe('');
    });

    test('t longer than s returns empty string', () => {
        expect(getMinimumWindowSubstring('ab', 'abc')).toBe('');
    });

    test('duplicate chars in t', () => {
        expect(getMinimumWindowSubstring('aab', 'aa')).toBe('aa');
    });

    test('exact match returns full string', () => {
        expect(getMinimumWindowSubstring('abc', 'abc')).toBe('abc');
    });

    test('multiple valid windows returns smallest', () => {
        expect(getMinimumWindowSubstring('cabwefgewcwaefgcf', 'cae')).toBe('cwae');
    });
});

"""
