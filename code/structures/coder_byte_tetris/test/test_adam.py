r"""TODO: port to Python.

Original JavaScript (code/structures/coder-byte-tetris/test/adam.test.js):

const { getMaxNumberOfRowsCleared } = require('../code/v2.js');

//  I: [[0,0], [0,1], [0,2], [0,3]],
//  O: [[0,0], [0,1], [1,0], [1,1]],
//  T: [[0,0], [0,1], [0,2], [1,1]],
//  S: [[0,0], [0,1], [1,1], [1,2]],
//  Z: [[0,1], [0,2], [1,0], [1,1]],
//  J: [[0,0], [0,1], [0,2], [1,2]]
//  L: [[0,0], [0,1], [0,2], [1,0]],

//  Row  6:             ██       ██       ██ ██
//  Row  5:          ██ ██       ██ ██    ██ ██
//  Row  4:    ██ ██ ██ ██       ██ ██    ██ ██
//  Row  3: ██ ██ ██ ██ ██       ██ ██ ██ ██ ██
//  Row  2: ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██
//  Row  1: ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██

describe('adams test cases - tetris', () => {
    describe('tetris test cases', () => {
        test('test case #1 => i', () => {
            const heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6];
            const result = getMaxNumberOfRowsCleared(heights, 'I');
            expect(result).toBe(2);
        });

        test('test case #2 => o', () => {
            const heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6];
            const result = getMaxNumberOfRowsCleared(heights, 'O');
            expect(result).toBe(1);
        });

        test('test case #3 => t', () => {
            const heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6];
            const result = getMaxNumberOfRowsCleared(heights, 'T');
            expect(result).toBe(2);
        });

        test('test case #4 => s', () => {
            const heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6];
            const result = getMaxNumberOfRowsCleared(heights, 'S');
            expect(result).toBe(1);
        });

        test('test case #5 => z', () => {
            const heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6];
            const result = getMaxNumberOfRowsCleared(heights, 'Z');
            expect(result).toBe(0);
        });

        test('test case #6 => j', () => {
            const heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6];
            const result = getMaxNumberOfRowsCleared(heights, 'J');
            expect(result).toBe(0);
        });

        test('test case #7 => l', () => {
            const heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6];
            const result = getMaxNumberOfRowsCleared(heights, 'L');
            expect(result).toBe(3);
        });
    });
});

"""
