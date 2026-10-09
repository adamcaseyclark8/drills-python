r"""TODO: port to Python.

Original JavaScript (test/graphs/word-ladder.test.js):

const wordLadderLength = require('../../code/graphs/word-ladder.js');

describe('word ladder length problem', () => {
    test('returns correct steps for a typical transformation', () => {
        const beginWord = 'hit';
        const endWord = 'cog';
        const wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog'];
        expect(wordLadderLength(beginWord, endWord, wordList)).toBe(5);
        // hit → hot → dot → dog → cog
    });

    test('returns 0 if end is not in list', () => {
        const beginWord = 'hit';
        const endWord = 'cog';
        const wordList = ['hot', 'dot', 'dog', 'lot', 'log']; // no 'cog'
        expect(wordLadderLength(beginWord, endWord, wordList)).toBe(0);
    });

    test('returns 0 if no path exists', () => {
        const beginWord = 'hit';
        const endWord = 'cog';
        const wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'xyz']; // 'cog' disconnected
        expect(wordLadderLength(beginWord, endWord, wordList)).toBe(0);
    });

    test('handles single letter words', () => {
        const beginWord = 'a';
        const endWord = 'c';
        const wordList = ['a', 'b', 'c'];
        expect(wordLadderLength(beginWord, endWord, wordList)).toBe(2);
        // a → c
    });

    test('begin equals end', () => {
        const beginWord = 'same';
        const endWord = 'same';
        const wordList = ['same', 'came', 'lame'];
        expect(wordLadderLength(beginWord, endWord, wordList)).toBe(1);
    });

    test('large transformation path', () => {
        const beginWord = 'hit';
        const endWord = 'cog';
        const wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog', 'hog', 'cot'];
        // multiple paths exist, shortest path length = 4
        expect(wordLadderLength(beginWord, endWord, wordList)).toBe(4);
        // hit → hot → hog → cog
    });

    test('empty word list', () => {
        const beginWord = 'hit';
        const endWord = 'cog';
        const wordList = [];
        expect(wordLadderLength(beginWord, endWord, wordList)).toBe(0);
    });
});

"""
