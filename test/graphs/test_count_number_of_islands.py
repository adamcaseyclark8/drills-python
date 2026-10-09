r"""TODO: port to Python.

Original JavaScript (test/graphs/count-number-of-islands.test.js):

const countNumberOfIslands = require('../../code/graphs/count-number-of-islands.js');

describe('count number of islands', () => {
    it('should return 0 for an empty grid', () => {
        expect(countNumberOfIslands([])).toBe(0);
    });

    it('should return 0 when there is only water', () => {
        const grid = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
        ];
        expect(countNumberOfIslands(grid)).toBe(0);
    });

    it('should return 1 when there is only one island', () => {
        const grid = [
            ['1', '1', '0'],
            ['1', '1', '0'],
            ['0', '0', '0']
        ];
        expect(countNumberOfIslands(grid)).toBe(1);
    });

    it('should return 3 for a grid with 3 separate islands', () => {
        const grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ];
        expect(countNumberOfIslands(grid)).toBe(3);
    });

    it('should handle diagonals not being connected', () => {
        const grid = [
            ['1', '0', '1'],
            ['0', '1', '0'],
            ['1', '0', '1']
        ];
        expect(countNumberOfIslands(grid)).toBe(5); // Diagonal connections don't count
    });

    it('should return correct count for a large single island', () => {
        const grid = [
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1']
        ];
        expect(countNumberOfIslands(grid)).toBe(1);
    });

    it('should not mutate original grid if needed (optional)', () => {
        const grid = [
            ['1', '1', '0'],
            ['1', '0', '0'],
            ['0', '0', '1']
        ];
        const deepCopy = JSON.parse(JSON.stringify(grid));
        countNumberOfIslands(grid);
        expect(grid).not.toEqual(deepCopy); // Optional test to remind mutation
    });
});

"""
