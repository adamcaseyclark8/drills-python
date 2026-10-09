r"""TODO: port to Python.

Original JavaScript (test/hashing/count-word-frequency.test.js):

const countWordFrequency = require('../../code/hashing/count-word-frequency.js');

describe('countWordFrequency', () => {
    describe('basic counting', () => {
        test('counts single word occurrences', () => {
            expect(countWordFrequency('the cat sat on the mat the cat')).toEqual({
                the: 3,
                cat: 2,
                sat: 1,
                on: 1,
                mat: 1
            });
        });

        test('counts single word', () => {
            expect(countWordFrequency('hello')).toEqual({ hello: 1 });
        });

        test('counts all unique words', () => {
            expect(countWordFrequency('one two three')).toEqual({
                one: 1,
                two: 1,
                three: 1
            });
        });
    });

    describe('case insensitivity', () => {
        test('treats uppercase and lowercase as the same word', () => {
            expect(countWordFrequency('The the THE')).toEqual({ the: 3 });
        });
    });

    describe('whitespace handling', () => {
        test('handles multiple spaces between words', () => {
            expect(countWordFrequency('hello   world')).toEqual({
                hello: 1,
                world: 1
            });
        });

        test('handles leading and trailing spaces', () => {
            expect(countWordFrequency('  hello world  ')).toEqual({
                hello: 1,
                world: 1
            });
        });
    });

    describe('edge cases', () => {
        test('returns empty object for empty string', () => {
            expect(countWordFrequency('')).toEqual({});
        });

        test('returns empty object for null', () => {
            expect(countWordFrequency(null)).toEqual({});
        });

        test('returns empty object for whitespace only', () => {
            expect(countWordFrequency('   ')).toEqual({});
        });
    });
});

"""
