r"""TODO: port to Python.

Original JavaScript (test/reimplementation/assertion-utils.test.js):

const { AssertionUtils } = require('../../code/reimplementation/assertion-utils.js');

describe('Assertion Utils Tests', () => {
    describe('assertEquals', () => {
        test('passes when values are equal', () => {
            expect(() => AssertionUtils.assertEquals('Adam', 'Adam', 'Names match')).not.toThrow();
        });

        test('throws when values are not equal', () => {
            expect(() => AssertionUtils.assertEquals('cat', 'dog', 'Should fail')).toThrow('FAIL');
        });
    });

    describe('assertTrue', () => {
        test('passes when condition is true', () => {
            expect(() => AssertionUtils.assertTrue(5 > 3, '5 is greater than 3')).not.toThrow();
        });

        test('throws when condition is false', () => {
            expect(() => AssertionUtils.assertTrue(2 > 10, 'Should fail')).toThrow('FAIL');
        });
    });

    describe('assertFalse', () => {
        test('passes when condition is false', () => {
            expect(() => AssertionUtils.assertFalse(2 > 10, '2 is not greater than 10')).not.toThrow();
        });

        test('throws when condition is true', () => {
            expect(() => AssertionUtils.assertFalse(5 > 3, 'Should fail')).toThrow('FAIL');
        });
    });

    describe('assertNull', () => {
        test('passes when value is null', () => {
            expect(() => AssertionUtils.assertIsNull(null, 'Value is null')).not.toThrow();
        });

        test('passes when value is undefined', () => {
            expect(() => AssertionUtils.assertIsNull(undefined, 'Value is undefined')).not.toThrow();
        });

        test('throws when value is not null', () => {
            expect(() => AssertionUtils.assertIsNull('hello', 'Should fail')).toThrow('FAIL');
        });
    });

    describe('assertNotNull', () => {
        test('passes when value is not null', () => {
            expect(() => AssertionUtils.assertIsNotNull('hello', 'Value is not null')).not.toThrow();
        });

        test('throws when value is null', () => {
            expect(() => AssertionUtils.assertIsNotNull(null, 'Should fail')).toThrow('FAIL');
        });
    });

    describe('assertNotEquals', () => {
        test('passes when values are not equal', () => {
            expect(() => AssertionUtils.assertNotEquals('cat', 'dog', 'Values differ')).not.toThrow();
        });

        test('throws when values are equal', () => {
            expect(() => AssertionUtils.assertNotEquals('cat', 'cat', 'Should fail')).toThrow('FAIL');
        });
    });

    describe('assertContains', () => {
        test('passes when string contains substring', () => {
            expect(() => AssertionUtils.assertContains('hello world', 'world', 'Contains world')).not.toThrow();
        });

        test('throws when string does not contain substring', () => {
            expect(() => AssertionUtils.assertContains('hello world', 'cats', 'Should fail')).toThrow('FAIL');
        });
    });

    describe('assertArrayEquals', () => {
        test('passes when arrays are equal', () => {
            expect(() => AssertionUtils.assertArrayEquals([1, 2, 3], [1, 2, 3], 'Arrays match')).not.toThrow();
        });

        test('throws when array lengths differ', () => {
            expect(() => AssertionUtils.assertArrayEquals([1, 2], [1, 2, 3], 'Should fail')).toThrow('FAIL');
        });

        test('throws when array values differ', () => {
            expect(() => AssertionUtils.assertArrayEquals([1, 2, 3], [1, 2, 9], 'Should fail')).toThrow('FAIL');
        });
    });
});

"""
