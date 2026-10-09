r"""TODO: port to Python.

Original JavaScript (test/dynamic-programming/longest-common-subsequence.test.js):

const longestCommonSubsequence = require('../../code/dynamic-programming/longest-common-subsequence.js');

describe('longestCommonSubsequence', () => {
    test('abcde and ace returns 3', () => {
        expect(longestCommonSubsequence('abcde', 'ace')).toBe(3);
    });

    test('abc and abc returns 3', () => {
        expect(longestCommonSubsequence('abc', 'abc')).toBe(3);
    });

    test('abc and def returns 0', () => {
        expect(longestCommonSubsequence('abc', 'def')).toBe(0);
    });

    test('empty strings returns 0', () => {
        expect(longestCommonSubsequence('', '')).toBe(0);
    });

    test('one empty string returns 0', () => {
        expect(longestCommonSubsequence('abc', '')).toBe(0);
    });

    test('single matching char returns 1', () => {
        expect(longestCommonSubsequence('a', 'a')).toBe(1);
    });

    test('single non-matching char returns 0', () => {
        expect(longestCommonSubsequence('a', 'b')).toBe(0);
    });

    test('bsbininm and jmjkbkjkv returns 1', () => {
        expect(longestCommonSubsequence('bsbininm', 'jmjkbkjkv')).toBe(1);
    });
});

"""
