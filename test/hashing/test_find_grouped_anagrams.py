r"""TODO: port to Python.

Original JavaScript (test/hashing/find-grouped-anagrams.test.js):

const findGroupedAnagrams = require('../../code/hashing/find-grouped-anagrams.js');

function sortGroupedAnagrams(output) {
    // Helper to normalize output for test comparison
    return output.map(group => group.sort()).sort((a, b) => a[0].localeCompare(b[0]));
}

describe('find grouped anagrams tests', () => {
    test('groups basic anagrams together', () => {
        const expected = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']];

        const result = findGroupedAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']);
        expect(sortGroupedAnagrams(result)).toEqual(sortGroupedAnagrams(expected));
    });

    test('returns empty array when input is empty', () => {
        expect(findGroupedAnagrams([])).toEqual([]);
    });

    test('no anagrams', () => {
        const result = findGroupedAnagrams(['cat', 'dog', 'bird']);
        expect(result).toEqual(expect.arrayContaining([['cat'], ['dog'], ['bird']]));
    });

    test('handles single word input', () => {
        expect(findGroupedAnagrams(['abc'])).toEqual([['abc']]);
    });

    test('handles all identical strings', () => {
        const input = ['aaa', 'aaa', 'aaa'];
        const expected = [['aaa', 'aaa', 'aaa']];
        expect(findGroupedAnagrams(input)).toEqual(expected);
    });

    test('all same anagram group', () => {
        const result = findGroupedAnagrams(['abc', 'bca', 'cab']);
        expect(result).toHaveLength(1);
        expect(result[0]).toEqual(expect.arrayContaining(['abc', 'bca', 'cab']));
    });

    test('treats words with different lengths as non-anagrams', () => {
        const input = ['ab', 'abc', 'a'];
        const expected = [['ab'], ['abc'], ['a']];
        expect(sortGroupedAnagrams(findGroupedAnagrams(input))).toEqual(sortGroupedAnagrams(expected));
    });

    test('handles mix of anagrams and non-anagrams', () => {
        const input = ['listen', 'silent', 'enlist', 'google', 'gooegl', 'abc'];
        const expected = [['abc'], ['enlist', 'listen', 'silent'], ['google', 'gooegl']];
        expect(sortGroupedAnagrams(findGroupedAnagrams(input))).toEqual(sortGroupedAnagrams(expected));
    });
});

"""
