r"""TODO: port to Python.

Original JavaScript (test/graphs/course-schedule.test.js):

const canFinishCourses = require('../../code/graphs/course-schedule.js');

describe('Course Schedule Algorithm', () => {
    test('returns true when no prerequisites', () => {
        expect(canFinishCourses(3, [])).toBe(true);
    });

    test('returns true for simple valid dependency chain', () => {
        const numCourses = 4;
        const prerequisites = [
            [1, 0],
            [2, 1],
            [3, 2]
        ];
        // Order: 0 -> 1 -> 2 -> 3
        expect(canFinishCourses(numCourses, prerequisites)).toBe(true);
    });

    test('returns false for simple cycle', () => {
        const numCourses = 2;
        const prerequisites = [
            [0, 1],
            [1, 0]
        ];
        // Cycle: 0 -> 1 -> 0
        expect(canFinishCourses(numCourses, prerequisites)).toBe(false);
    });

    test('returns false for larger cycle', () => {
        const numCourses = 4;
        const prerequisites = [
            [1, 0],
            [2, 1],
            [0, 2]
        ];
        // Cycle: 0 -> 1 -> 2 -> 0
        expect(canFinishCourses(numCourses, prerequisites)).toBe(false);
    });

    test('returns true for multiple independent chains', () => {
        const numCourses = 6;
        const prerequisites = [
            [1, 0], // chain 1: 0 -> 1
            [3, 2], // chain 2: 2 -> 3
            [5, 4] // chain 3: 4 -> 5
        ];
        expect(canFinishCourses(numCourses, prerequisites)).toBe(true);
    });

    test('returns true for complex valid graph with branches', () => {
        const numCourses = 5;
        const prerequisites = [
            [1, 0],
            [2, 0],
            [3, 1],
            [3, 2],
            [4, 3]
        ];
        // Valid order exists: 0 -> 1/2 -> 3 -> 4
        expect(canFinishCourses(numCourses, prerequisites)).toBe(true);
    });

    test('returns false when single course depends on itself', () => {
        const numCourses = 1;
        const prerequisites = [[0, 0]];
        expect(canFinishCourses(numCourses, prerequisites)).toBe(false);
    });

    test('handles disconnected graph with one cycle', () => {
        const numCourses = 5;
        const prerequisites = [
            [1, 0],
            [2, 1],
            [0, 2], // cycle in subgraph
            [4, 3] // separate valid subgraph
        ];
        expect(canFinishCourses(numCourses, prerequisites)).toBe(false);
    });
});

"""
