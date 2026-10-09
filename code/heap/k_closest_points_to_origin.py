r"""TODO: port to Python.

Original JavaScript (code/heap/k-closest-points-to-origin.js):

const findKClosestPointsToOrigin = (points, k) => {
    const dist = p => p[0] ** 2 + p[1] ** 2;

    return points.sort((a, b) => dist(a) - dist(b)).slice(0, k);
};

module.exports = findKClosestPointsToOrigin;

"""
