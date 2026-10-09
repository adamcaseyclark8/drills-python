r"""TODO: port to Python.

Original JavaScript (code/sorting/merge-overlapping-arrays.js):

const mergeOverlappingArrays = intervals => {
    if (intervals.length === 0) return [];

    // Sort intervals by their start times
    intervals.sort((a, b) => a[0] - b[0]);

    const merged = [];
    // Start with the first interval
    merged.push(intervals[0]);

    for (let i = 1; i < intervals.length; i++) {
        const current = intervals[i];
        const lastMerged = merged[merged.length - 1];

        // Check if current overlaps with the last merged interval
        if (current[0] <= lastMerged[1]) {
            // Merge by updating the end of the last merged interval if needed
            lastMerged[1] = Math.max(lastMerged[1], current[1]);
        } else {
            // No overlap, just add the current interval
            merged.push(current);
        }
    }

    return merged;
};

module.exports = mergeOverlappingArrays;

"""
