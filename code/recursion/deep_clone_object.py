r"""TODO: port to Python.

Original JavaScript (code/recursion/deep-clone-object.js):

const deepCloneObject = object => {
    if (object === null || typeof object !== 'object') return object;
    if (Array.isArray(object)) return object.map(item => deepCloneObject(item));
    return Object.keys(object).reduce((acc, key) => {
        acc[key] = deepCloneObject(object[key]);
        return acc;
    }, {});
};

module.exports = deepCloneObject;

"""
