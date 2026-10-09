r"""TODO: port to Python.

Original JavaScript (test/two-pointers/code-signal-container-exercise.test.js):

const codeSignalContainerExercise = require('../../code/two-pointers/code-signal-container-exercise.js');

const ADD = 'ADD';
const EXISTS = 'EXISTS';
const REMOVE = 'REMOVE';
const NEXT_UP = 'NEXT_UP';

describe('code signal container exercise', () => {
    test('I: add', () => {
        const queries = [
            [ADD, '1'],
            [ADD, '2'],
            [ADD, '3'],
            [ADD, '4'],
            [ADD, '5']
        ];

        const output = codeSignalContainerExercise(queries);
        const answer = ['', '', '', '', ''];

        expect(output).toStrictEqual(answer);
    });

    test('II: exists', () => {
        const queries = [
            [ADD, '1'],
            [ADD, '2'],
            [EXISTS, '1'],
            [EXISTS, '2'],
            [EXISTS, '3']
        ];

        const output = codeSignalContainerExercise(queries);
        const answer = ['', '', 'true', 'true', 'false'];

        expect(output).toStrictEqual(answer);
    });

    test('III: remove', () => {
        const queries = [
            [ADD, '1'],
            [ADD, '2'],
            [ADD, '3'],
            [ADD, '4'],
            [REMOVE, '2'],
            [EXISTS, '2'],
            [REMOVE, '4'],
            [EXISTS, '4'],
            [EXISTS, '3']
        ];

        const output = codeSignalContainerExercise(queries);
        const answer = ['', '', '', '', 'true', 'false', 'true', 'false', 'true'];
        expect(output).toStrictEqual(answer);
    });

    test('IV: next up', () => {
        const queries = [
            [ADD, '1'],
            [ADD, '5'],
            [ADD, '6'],
            [ADD, '9'],
            [NEXT_UP, '1'],
            [NEXT_UP, '5'],
            [NEXT_UP, '6'],
            [NEXT_UP, '9']
        ];

        const output = codeSignalContainerExercise(queries);
        const answer = ['', '', '', '', '5', '6', '9', ''];
        expect(output).toStrictEqual(answer);
    });
});

"""
