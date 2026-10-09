r"""TODO: port to Python.

Original JavaScript (code/greedy/perform-activity-selection.js):

const performActivitySelection = activities => {
    const sorted = [...activities].sort((a, b) => a.end - b.end);
    const selected = [sorted[0]];
    let lastEnd = sorted[0].end;

    for (let i = 1; i < sorted.length; i++) {
        if (sorted[i].start >= lastEnd) {
            selected.push(sorted[i]);
            lastEnd = sorted[i].end;
        }
    }

    return selected;
};

module.exports = performActivitySelection;

"""
