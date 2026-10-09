r"""TODO: port to Python.

Original JavaScript (test/hashing/first-unique-character.test.js):

const findFirstUniqueCharacter = require('../../code/hashing/first-unique-character.js');

describe('findFirstUniqueCharacter', () => {
    test('finds first unique in basic string', () => {
        expect(findFirstUniqueCharacter('leetcode')).toBe(0);
    });

    test('finds unique not at start', () => {
        expect(findFirstUniqueCharacter('loveleetcode')).toBe(2);
    });

    test('returns -1 if no unique char', () => {
        expect(findFirstUniqueCharacter('aabb')).toBe(-1);
    });

    test('handles single character', () => {
        expect(findFirstUniqueCharacter('z')).toBe(0);
    });

    test('handles repeated single character', () => {
        expect(findFirstUniqueCharacter('zzzz')).toBe(-1);
    });

    test('works with mixed case (case-sensitive)', () => {
        expect(findFirstUniqueCharacter('aA')).toBe(0); // 'a' !== 'A'
    });

    test('works with spaces and symbols', () => {
        // string: [space, space, !, !, a, b, a, c]
        // indices: 0,1,2,3,4,5,6,7  => 'b' at index 5 is first unique
        expect(findFirstUniqueCharacter('  !!abac')).toBe(5);
    });

    test('returns -1 for empty string', () => {
        expect(findFirstUniqueCharacter('')).toBe(-1);
    });

    test('handles all unique chars', () => {
        expect(findFirstUniqueCharacter('abcdef')).toBe(0);
    });

    test('first unique in long string', () => {
        // 'aabbccddeefggh' -> f at index 10 is first unique
        expect(findFirstUniqueCharacter('aabbccddeefggh')).toBe(10);
    });
});

"""
