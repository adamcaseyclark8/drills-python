r"""TODO: port to Python.

Original JavaScript (test/greedy/perform-activity-selection.test.js):

const performActivitySelection = require('../../code/greedy/perform-activity-selection.js');

describe('perform activity selection test', () => {
    test('returns maximum non-overlapping activities', () => {
        const activities = [
            { start: 1, end: 4 },
            { start: 3, end: 5 },
            { start: 0, end: 6 },
            { start: 5, end: 7 },
            { start: 3, end: 9 },
            { start: 6, end: 10 },
            { start: 8, end: 11 },
            { start: 8, end: 12 },
            { start: 2, end: 14 },
            { start: 12, end: 16 }
        ];
        const result = performActivitySelection(activities);
        expect(result).toHaveLength(4);
    });

    test('single activity returns itself', () => {
        expect(performActivitySelection([{ start: 1, end: 2 }])).toEqual([{ start: 1, end: 2 }]);
    });

    test('non-overlapping activities returns all', () => {
        const activities = [
            { start: 1, end: 2 },
            { start: 3, end: 4 },
            { start: 5, end: 6 }
        ];
        expect(performActivitySelection(activities)).toHaveLength(3);
    });

    test('all overlapping returns only one', () => {
        const activities = [
            { start: 1, end: 10 },
            { start: 2, end: 9 },
            { start: 3, end: 8 }
        ];
        expect(performActivitySelection(activities)).toHaveLength(1);
    });

    test('does not mutate input', () => {
        const activities = [
            { start: 3, end: 5 },
            { start: 1, end: 4 }
        ];
        const copy = [...activities];
        performActivitySelection(activities);
        expect(activities).toEqual(copy);
    });

    test('adjacent activities are selected', () => {
        const activities = [
            { start: 0, end: 2 },
            { start: 2, end: 4 },
            { start: 4, end: 6 }
        ];
        expect(performActivitySelection(activities)).toHaveLength(3);
    });
});

"""
