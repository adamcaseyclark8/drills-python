r"""TODO: port to Python.

Original JavaScript (misc/helpers/flatmap.js):

const arr = [1, 2, 3, 4];

const x = arr.map(x => [x * 2]);
// [[2], [4], [6], [8]]

const y = arr.flatMap(x => [x * 2]);
// [2, 4, 6, 8]

// only one level is flattened
const z = arr.flatMap(x => [[x * 2]]);
// [[2], [4], [6], [8]]

console.log(x);
console.log(y);
console.log(z);

"""
