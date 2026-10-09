r"""TODO: port to Python.

Original JavaScript (test/greedy/perform-column-addition.test.js):

const performColumnAddition = require('../../code/greedy/perform-column-addition');

describe('perform column addition tests', () => {
    test('456 + 77 returns 533', () => {
        expect(performColumnAddition('456', '77')).toBe('533');
    });

    test('11 + 123 returns 134', () => {
        expect(performColumnAddition('11', '123')).toBe('134');
    });

    test('999 + 1 returns 1000', () => {
        expect(performColumnAddition('999', '1')).toBe('1000');
    });

    test('0 + 0 returns 0', () => {
        expect(performColumnAddition('0', '0')).toBe('0');
    });

    test('same length no carry', () => {
        expect(performColumnAddition('123', '456')).toBe('579');
    });

    test('large numbers', () => {
        expect(performColumnAddition('9999999999', '1')).toBe('10000000000');
    });

    test('single digits with carry', () => {
        expect(performColumnAddition('9', '9')).toBe('18');
    });

    test('one number is zero', () => {
        expect(performColumnAddition('500', '0')).toBe('500');
    });
});

"""
