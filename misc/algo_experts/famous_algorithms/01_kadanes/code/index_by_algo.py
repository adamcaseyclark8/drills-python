r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/famous-algorithms/01-kadanes/code/index-by-algo.js):

function Kadanes(array) {
    let maxEndingHere = array[0];
    let maxSoFar = array[0];

    for (let i = 1; i < array.length; i++) {
        const num = array[i];
        maxEndingHere = Math.max(num, maxEndingHere + num);
        maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }
    return maxSoFar;
}

exports.Kadanes = Kadanes;

"""
