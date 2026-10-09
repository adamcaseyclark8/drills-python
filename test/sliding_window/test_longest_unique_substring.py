r"""TODO: port to Python.

Original JavaScript (test/sliding-window/longest-unique-substring.test.js):

const longestUniqueSubstring = require('../../code/sliding-window/longest-unique-substring.js');

describe('verify longest unique substring', () => {
    test('standard scenario', () => {
        expect(longestUniqueSubstring('geeksforgeeks')).toBe('eksforg');
    });

    test('repeating exact same twice', () => {
        expect(longestUniqueSubstring('abcabcbb')).toBe('abc');
    });

    test('same character repeated', () => {
        expect(longestUniqueSubstring('bbbbb')).toBe('b');
    });

    test('will not be pwke - will be wke', () => {
        expect(longestUniqueSubstring('pwwkew')).toBe('wke');
    });

    test('basic case', () => {
        expect(longestUniqueSubstring('abcabcbb')).toBe('abc');
    });

    test('all unique', () => {
        expect(longestUniqueSubstring('abcdef')).toBe('abcdef');
    });

    test('all same characters', () => {
        expect(longestUniqueSubstring('aaaa')).toBe('a');
    });

    test('empty string', () => {
        expect(longestUniqueSubstring('')).toBe('');
    });

    test('single character', () => {
        expect(longestUniqueSubstring('a')).toBe('a');
    });

    test('unique at end', () => {
        expect(longestUniqueSubstring('aabcd')).toBe('abcd');
    });
});

"""
