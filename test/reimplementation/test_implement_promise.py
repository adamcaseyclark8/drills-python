r"""TODO: port to Python.

Original JavaScript (test/reimplementation/implement-promise.test.js):

const { delay, fetchWithRetry } = require('../../code/reimplementation/implement-promise.js');

describe('delay', () => {
    test('resolves with value after ms', async () => {
        const result = await delay(50, 'hello');
        expect(result).toBe('hello');
    });

    test('resolves after the specified time', async () => {
        const start = Date.now();
        await delay(100, null);
        expect(Date.now() - start).toBeGreaterThanOrEqual(100);
    });
});

describe('fetchWithRetry', () => {
    test('resolves immediately on first success', async () => {
        const fn = jest.fn().mockResolvedValue('ok');
        const result = await fetchWithRetry(fn, 3);
        expect(result).toBe('ok');
        expect(fn).toHaveBeenCalledTimes(1);
    });

    test('retries on failure and eventually resolves', async () => {
        const fn = jest
            .fn()
            .mockRejectedValueOnce(new Error('fail'))
            .mockRejectedValueOnce(new Error('fail'))
            .mockResolvedValue('ok');
        const result = await fetchWithRetry(fn, 3);
        expect(result).toBe('ok');
        expect(fn).toHaveBeenCalledTimes(3);
    });

    test('rejects after all retries exhausted', async () => {
        const fn = jest.fn().mockRejectedValue(new Error('always fails'));
        await expect(fetchWithRetry(fn, 2)).rejects.toThrow('always fails');
        expect(fn).toHaveBeenCalledTimes(3);
    });

    test('resolves with 0 retries if first call succeeds', async () => {
        const fn = jest.fn().mockResolvedValue('done');
        const result = await fetchWithRetry(fn, 0);
        expect(result).toBe('done');
    });

    test('rejects immediately with 0 retries on failure', async () => {
        const fn = jest.fn().mockRejectedValue(new Error('nope'));
        await expect(fetchWithRetry(fn, 0)).rejects.toThrow('nope');
        expect(fn).toHaveBeenCalledTimes(1);
    });
});

"""
