r"""TODO: port to Python.

Original JavaScript (test/hashing/verify-valid-anagram.test.js):

const verifyValidAnagram = require('../../code/hashing/verify-valid-anagram.js');

describe('valid anagrams=', () => {
    test('scenario with valid anagram', () => {
        expect(verifyValidAnagram('cinema', 'iceman')).toBe(true);
    });

    test('not a valid anagram', () => {
        expect(verifyValidAnagram('cinema', 'icemen')).toBe(false);
    });

    test('unequal strings', () => {
        expect(verifyValidAnagram('cinema', 'icemann')).toBe(false);
    });

    test('another variation of false', () => {
        expect(verifyValidAnagram('cinemaa', 'icemann')).toBe(false);
    });
});

"""
