r"""TODO: port to Python.

Original JavaScript (test/hashing/get-most-frequent-element.test.js):

const getMostFrequentElement = require('../../code/hashing/get-most-frequent-element');

// THE FIRST ENCOUNTERED MOST ELEMENT IF TIED

test('returns most frequent element', () => {
    expect(getMostFrequentElement(['a', 'b', 'a', 'c', 'a', 'b'])).toBe('a');
});

test('single element array', () => {
    expect(getMostFrequentElement(['x'])).toBe('x');
});

test('all same elements', () => {
    expect(getMostFrequentElement(['z', 'z', 'z'])).toBe('z');
});

test('numbers', () => {
    expect(getMostFrequentElement([1, 2, 2, 3, 2])).toBe(2);
});

test('tie returns first most frequent encountered', () => {
    expect(getMostFrequentElement(['a', 'b', 'b', 'a'])).toBe('a');
});

"""
