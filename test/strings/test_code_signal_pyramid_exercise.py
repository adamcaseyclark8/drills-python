r"""TODO: port to Python.

Original JavaScript (test/strings/code-signal-pyramid-exercise.test.js):

const buildAsciiPyramid = require('../../code/strings/code-signal-pyramid-exercise.js');

describe('buildAsciiPyramid', () => {
    let consoleSpy;

    beforeEach(() => {
        consoleSpy = jest.spyOn(console, 'log').mockImplementation();
    });

    afterEach(() => {
        consoleSpy.mockRestore();
    });

    test('creates a buildAsciiPyramid with n=1', () => {
        buildAsciiPyramid(1);
        expect(consoleSpy).toHaveBeenCalledTimes(1);
        expect(consoleSpy).toHaveBeenCalledWith('*');
    });

    test('creates a buildAsciiPyramid with n=3', () => {
        buildAsciiPyramid(3);
        expect(consoleSpy).toHaveBeenCalledTimes(3);
        expect(consoleSpy.mock.calls[0][0]).toBe('  *');
        expect(consoleSpy.mock.calls[1][0]).toBe(' ***');
        expect(consoleSpy.mock.calls[2][0]).toBe('*****');
    });

    test('creates a buildAsciiPyramid with n=5', () => {
        buildAsciiPyramid(5);
        expect(consoleSpy).toHaveBeenCalledTimes(5);
        expect(consoleSpy.mock.calls[0][0]).toBe('    *');
        expect(consoleSpy.mock.calls[1][0]).toBe('   ***');
        expect(consoleSpy.mock.calls[2][0]).toBe('  *****');
        expect(consoleSpy.mock.calls[3][0]).toBe(' *******');
        expect(consoleSpy.mock.calls[4][0]).toBe('*********');
    });

    test('creates a buildAsciiPyramid with n=10', () => {
        buildAsciiPyramid(10);
        expect(consoleSpy).toHaveBeenCalledTimes(10);
        expect(consoleSpy.mock.calls[0][0]).toBe('         *');
        expect(consoleSpy.mock.calls[9][0]).toBe('*******************');
    });

    test('each row has correct number of leading spaces and asterisks', () => {
        const n = 7;
        buildAsciiPyramid(n);

        for (let i = 0; i < n; i++) {
            const row = consoleSpy.mock.calls[i][0];
            const spaces = n - (i + 1);
            const asterisks = 2 * (i + 1) - 1;

            expect(row).toBe(' '.repeat(spaces) + '*'.repeat(asterisks));
        }
    });

    test('each row has correct number of asterisks', () => {
        const n = 5;
        buildAsciiPyramid(n);

        for (let i = 0; i < n; i++) {
            const row = consoleSpy.mock.calls[i][0];
            const asteriskCount = (row.match(/\*/g) || []).length;
            expect(asteriskCount).toBe(2 * (i + 1) - 1);
        }
    });

    test('first row has only one asterisk', () => {
        buildAsciiPyramid(4);
        const firstRow = consoleSpy.mock.calls[0][0];
        expect(firstRow.trim()).toBe('*');
    });

    test('last row has no leading spaces', () => {
        buildAsciiPyramid(6);
        const lastRow = consoleSpy.mock.calls[5][0];
        expect(lastRow[0]).toBe('*');
    });
});

"""
