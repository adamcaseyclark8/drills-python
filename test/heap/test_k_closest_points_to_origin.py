r"""TODO: port to Python.

Original JavaScript (test/heap/k-closest-points-to-origin.test.js):

const findKClosestPointsToOrigin = require('../../code/heap/k-closest-points-to-origin');

describe('find k closest points to origin', () => {
    test('basic case - k=1', () => {
        expect(
            findKClosestPointsToOrigin(
                [
                    [1, 3],
                    [-2, 2]
                ],
                1
            )
        ).toEqual([[-2, 2]]);
    });

    test('basic case - k=2', () => {
        const result = findKClosestPointsToOrigin(
            [
                [3, 3],
                [5, -1],
                [-2, 4]
            ],
            2
        );
        expect(result).toHaveLength(2);
        expect(result).toContainEqual([3, 3]);
        expect(result).toContainEqual([-2, 4]);
    });

    test('k equals total number of points', () => {
        const points = [
            [1, 1],
            [2, 2],
            [3, 3]
        ];
        expect(findKClosestPointsToOrigin(points, 3)).toHaveLength(3);
    });

    test('point at origin is always closest', () => {
        const result = findKClosestPointsToOrigin(
            [
                [0, 0],
                [1, 1],
                [2, 2]
            ],
            1
        );
        expect(result).toEqual([[0, 0]]);
    });

    test('negative coordinates', () => {
        const result = findKClosestPointsToOrigin(
            [
                [-1, -1],
                [-5, -5],
                [0, 1]
            ],
            1
        );
        expect(result).toContainEqual([0, 1]);
    });

    test('points equidistant - returns k of them', () => {
        const result = findKClosestPointsToOrigin(
            [
                [1, 0],
                [0, 1],
                [-1, 0],
                [0, -1]
            ],
            2
        );
        expect(result).toHaveLength(2);
    });

    test('large k', () => {
        const points = [
            [1, 2],
            [3, 4],
            [5, 6],
            [0, 1]
        ];
        expect(findKClosestPointsToOrigin(points, 4)).toHaveLength(4);
    });
});

"""
