r"""TODO: port to Python.

Original JavaScript (test/strings/count-vowels-and-consonants.test.js):

const countVowelsAndConsonants = require('../../code/strings/count-vowels-and-consonants.js');

describe('countVowelsAndConsonants', () => {
    describe('basic cases', () => {
        test('"hello" → 2 vowels, 3 consonants', () => {
            expect(countVowelsAndConsonants('hello')).toEqual({ vowels: 2, consonants: 3 });
        });

        test('"javascript" → 3 vowels, 7 consonants', () => {
            expect(countVowelsAndConsonants('javascript')).toEqual({ vowels: 3, consonants: 7 });
        });

        test('"aeiou" → 5 vowels, 0 consonants', () => {
            expect(countVowelsAndConsonants('aeiou')).toEqual({ vowels: 5, consonants: 0 });
        });

        test('"rhythm" → 0 vowels, 6 consonants', () => {
            expect(countVowelsAndConsonants('rhythm')).toEqual({ vowels: 0, consonants: 6 });
        });
    });

    describe('case insensitivity', () => {
        test('"HELLO" → 2 vowels, 3 consonants', () => {
            expect(countVowelsAndConsonants('HELLO')).toEqual({ vowels: 2, consonants: 3 });
        });

        test('"JavaScript" → 3 vowels, 7 consonants', () => {
            expect(countVowelsAndConsonants('JavaScript')).toEqual({ vowels: 3, consonants: 7 });
        });
    });

    describe('non-letter characters are ignored', () => {
        test('"hello world" → spaces ignored', () => {
            expect(countVowelsAndConsonants('hello world')).toEqual({ vowels: 3, consonants: 7 });
        });

        test('"h3ll0!" → numbers and symbols ignored', () => {
            expect(countVowelsAndConsonants('h3ll0!')).toEqual({ vowels: 0, consonants: 3 });
        });

        test('"a1b2c3" → only letters counted', () => {
            expect(countVowelsAndConsonants('a1b2c3')).toEqual({ vowels: 1, consonants: 2 });
        });
    });

    describe('edge cases', () => {
        test('empty string → 0 vowels, 0 consonants', () => {
            expect(countVowelsAndConsonants('')).toEqual({ vowels: 0, consonants: 0 });
        });

        test('string with only spaces → 0 vowels, 0 consonants', () => {
            expect(countVowelsAndConsonants('   ')).toEqual({ vowels: 0, consonants: 0 });
        });

        test('single vowel "a" → 1 vowel, 0 consonants', () => {
            expect(countVowelsAndConsonants('a')).toEqual({ vowels: 1, consonants: 0 });
        });

        test('single consonant "b" → 0 vowels, 1 consonant', () => {
            expect(countVowelsAndConsonants('b')).toEqual({ vowels: 0, consonants: 1 });
        });
    });
});

"""
