r"""TODO: port to Python.

Original JavaScript (test/arrays/increment-number-representation.test.js):

const incrementNumberRepresentation = require('../../code/arrays/increment-number-representation.js');

describe('incrementNumberRepresentation', () => {
    describe('basic increments', () => {
        test('[1, 2, 9] → [1, 3, 0]', () => {
            expect(incrementNumberRepresentation([1, 2, 9])).toEqual([1, 3, 0]);
        });

        test('[1, 2, 3] → [1, 2, 4]', () => {
            expect(incrementNumberRepresentation([1, 2, 3])).toEqual([1, 2, 4]);
        });

        test('[0] → [1]', () => {
            expect(incrementNumberRepresentation([0])).toEqual([1]);
        });

        test('[8] → [9]', () => {
            expect(incrementNumberRepresentation([8])).toEqual([9]);
        });
    });

    describe('carry propagation', () => {
        test('[9] → [1, 0]', () => {
            expect(incrementNumberRepresentation([9])).toEqual([1, 0]);
        });

        test('[9, 9, 9] → [1, 0, 0, 0]', () => {
            expect(incrementNumberRepresentation([9, 9, 9])).toEqual([1, 0, 0, 0]);
        });

        test('[1, 9, 9] → [2, 0, 0]', () => {
            expect(incrementNumberRepresentation([1, 9, 9])).toEqual([2, 0, 0]);
        });

        test('[2, 9] → [3, 0]', () => {
            expect(incrementNumberRepresentation([2, 9])).toEqual([3, 0]);
        });
    });

    describe('edge cases', () => {
        test('single zero [0] → [1]', () => {
            expect(incrementNumberRepresentation([0])).toEqual([1]);
        });

        test('large all-nines [9, 9, 9, 9, 9] → [1, 0, 0, 0, 0, 0]', () => {
            expect(incrementNumberRepresentation([9, 9, 9, 9, 9])).toEqual([1, 0, 0, 0, 0, 0]);
        });

        test('does not mutate original array', () => {
            const input = [1, 2, 9];
            incrementNumberRepresentation(input);
            expect(input).toEqual([1, 2, 9]);
        });
    });
});

"""
