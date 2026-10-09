r"""TODO: port to Python.

Original JavaScript (test/strings/compress-string-into-char-counts.test.js):

const compressStringIntoCharCounts = require('../../code/strings/compress-string-into-char-counts.js');

describe('compressStringIntoCharCounts', () => {
    describe('basic compression', () => {
        test('compresses repeated characters', () => {
            expect(compressStringIntoCharCounts('aabcccdddd')).toBe('a2b1c3d4');
        });

        test('compresses all same characters', () => {
            expect(compressStringIntoCharCounts('aaaaaaa')).toBe('a7');
        });

        test('compresses two groups', () => {
            expect(compressStringIntoCharCounts('aaabbb')).toBe('a3b3');
        });
    });

    describe('no compression needed', () => {
        test('returns original if compressed is not smaller', () => {
            expect(compressStringIntoCharCounts('aabbcc')).toBe('aabbcc');
        });

        test('returns original if all characters are unique', () => {
            expect(compressStringIntoCharCounts('abcd')).toBe('abcd');
        });
    });

    describe('4 edge cases', () => {
        test('returns empty string for empty input', () => {
            expect(compressStringIntoCharCounts('')).toBe('');
        });

        test('returns null for null input', () => {
            expect(compressStringIntoCharCounts(null)).toBe(null);
        });

        test('handles single character', () => {
            expect(compressStringIntoCharCounts('a')).toBe('a');
        });

        test('handles single repeated character', () => {
            expect(compressStringIntoCharCounts('aa')).toBe('aa');
        });
    });
});

"""
