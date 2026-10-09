r"""TODO: port to Python.

Original JavaScript (test/backtracking/permutations-of-an-array.test.js):

const permutationsOfAnArray = require('../../code/backtracking/permutations-of-an-array.js');

// Helper: sort a list of arrays for order-independent comparison
const sort = arr => arr.map(p => [...p]).sort((a, b) => (a.join() > b.join() ? 1 : -1));

describe('permutationsOfAnArray (backtracking)', () => {
    test('empty array returns one empty permutation', () => {
        expect(permutationsOfAnArray([])).toEqual([[]]);
    });

    test('single element returns one permutation', () => {
        expect(permutationsOfAnArray([1])).toEqual([[1]]);
    });

    test('two elements returns 2 permutationsOfAnArray', () => {
        expect(sort(permutationsOfAnArray([1, 2]))).toEqual(
            sort([
                [1, 2],
                [2, 1]
            ])
        );
    });

    test('three elements returns 6 permutationsOfAnArray', () => {
        const result = permutationsOfAnArray([1, 2, 3]);

        // Correct count: 3! = 6
        expect(result).toHaveLength(6);

        // Contains every expected arrangement
        const expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ];
        expect(sort(result)).toEqual(sort(expected));
    });

    test('four elements returns 24 permutationsOfAnArray', () => {
        expect(permutationsOfAnArray([1, 2, 3, 4])).toHaveLength(24); // 4! = 24
    });

    test('no duplicate permutationsOfAnArray are produced', () => {
        const result = permutationsOfAnArray([1, 2, 3]);
        const unique = new Set(result.map(p => p.join(',')));
        expect(unique.size).toBe(result.length);
    });

    test('each permutation contains all original elements', () => {
        const input = [4, 5, 6];
        const sorted = [...input].sort();
        for (const perm of permutationsOfAnArray(input)) {
            expect([...perm].sort((a, b) => a - b)).toEqual(sorted);
        }
    });

    test('works with non-numeric values', () => {
        const result = permutationsOfAnArray(['a', 'b', 'c']);
        expect(result).toHaveLength(6);
        expect(result).toContainEqual(['a', 'b', 'c']);
        expect(result).toContainEqual(['c', 'b', 'a']);
    });

    test('does not mutate the input array', () => {
        const input = [1, 2, 3];
        const copy = [...input];
        permutationsOfAnArray(input);
        expect(input).toEqual(copy);
    });
});

"""
