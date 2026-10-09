r"""TODO: port to Python.

Original JavaScript (test/matrices/verify-tic-tac-toe.test.js):

const calculateWinnerInTicTacToe = require('../../code/matrices/verify-tic-tac-toe.js');

describe('calculate winner in tic tac toe', () => {
    test('returns X for a winning row', () => {
        const squares = ['X', 'X', 'X', 'O', null, 'O', null, null, null];
        expect(calculateWinnerInTicTacToe(squares)).toBe('X');
    });

    test('returns O for a winning column', () => {
        const squares = ['O', 'X', null, 'O', 'X', null, 'O', null, 'X'];
        expect(calculateWinnerInTicTacToe(squares)).toBe('O');
    });

    test('returns X for a winning diagonal (top-left to bottom-right)', () => {
        const squares = ['X', 'O', null, null, 'X', 'O', null, null, 'X'];
        expect(calculateWinnerInTicTacToe(squares)).toBe('X');
    });

    test('returns O for a winning diagonal (top-right to bottom-left)', () => {
        const squares = ['X', null, 'O', null, 'O', 'X', 'O', null, null];
        expect(calculateWinnerInTicTacToe(squares)).toBe('O');
    });

    test('returns null when there is no winner yet', () => {
        const squares = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O'];
        // board full, but no 3-in-a-row
        expect(calculateWinnerInTicTacToe(squares)).toBe(null);
    });

    test('returns null for an empty board', () => {
        const squares = Array(9).fill(null);
        expect(calculateWinnerInTicTacToe(squares)).toBe(null);
    });

    test('returns the first winning line found (top priority)', () => {
        // Multiple lines possible, function stops at the first match
        const squares = [
            'X',
            'X',
            'X', // row 1 win
            'X',
            'X',
            'X', // row 2 also win
            'O',
            'O',
            'O'
        ];
        // According to code order, first win found is top row
        expect(calculateWinnerInTicTacToe(squares)).toBe('X');
    });
});

"""
