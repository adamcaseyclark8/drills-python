r"""TODO: port to Python.

Original JavaScript (test/recursion/deep-clone-object.test.js):

const deepCloneObject = require('../../code/recursion/deep-clone-object');

test('basic shallow object', () => {
    const obj = { a: 1, b: 2 };
    const clone = deepCloneObject(obj);
    expect(clone).toEqual(obj);
    expect(clone).not.toBe(obj);
});

test('nested object is a new reference', () => {
    const obj = { a: 1, b: { c: 2 } };
    const clone = deepCloneObject(obj);
    expect(clone).toEqual(obj);
    expect(clone.b).not.toBe(obj.b);
});

test('nested arrays', () => {
    const obj = { a: [1, 2, 3] };
    const clone = deepCloneObject(obj);
    expect(clone).toEqual(obj);
    expect(clone.a).not.toBe(obj.a);
});

test('deeply nested object', () => {
    const obj = { a: { b: { c: { d: 4 } } } };
    const clone = deepCloneObject(obj);
    expect(clone).toEqual(obj);
    expect(clone.a.b.c).not.toBe(obj.a.b.c);
});

test('null value', () => {
    expect(deepCloneObject(null)).toBeNull();
});

test('primitive value', () => {
    expect(deepCloneObject(42)).toBe(42);
});

test('array of objects', () => {
    const obj = [{ a: 1 }, { b: 2 }];
    const clone = deepCloneObject(obj);
    expect(clone).toEqual(obj);
    expect(clone[0]).not.toBe(obj[0]);
});

"""
