r"""TODO: port to Python.

Original JavaScript (code/reimplementation/implement-promise.js):

const delay = (ms, value) => new Promise(resolve => setTimeout(() => resolve(value), ms));

const fetchWithRetry = (fn, retries) =>
    fn().catch(err => {
        if (retries <= 0) return Promise.reject(err);
        return fetchWithRetry(fn, retries - 1);
    });

module.exports = { delay, fetchWithRetry };

"""
