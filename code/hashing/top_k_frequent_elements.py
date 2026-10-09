r"""TODO: port to Python.

Original JavaScript (code/hashing/top-k-frequent-elements.js):

const getTopKFrequentElements = (nums, k) => {
    const frequencyMap = new Map();

    // Step 1: Count frequencies
    for (let num of nums) {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    }

    // Step 2: Bucket sort - array index represents frequency
    const bucket = Array(nums.length + 1)
        .fill()
        .map(() => []);

    // console.log('frequency map', '\n', frequencyMap);
    // console.log('bucket v1', '\n', bucket);

    // [5, 3, 1, 1, 1, 3, 5, 5, 5]
    // {5: 4, 1: 3, 3: 2}
    // [[],[],[3],[1],[5],[],[],[],[]]

    for (let [num, freq] of frequencyMap.entries()) {
        bucket[freq].push(num);
    }

    // console.log('bucket v2', '\n', bucket);

    // Step 3: Collect top k frequent elements
    const result = [];

    // console.log('bucket length', bucket.length);

    for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
        if (bucket[i].length > 0) {
            result.push(...bucket[i]);
        }
    }

    // console.log('result', '\n', result)

    return result.slice(0, k); // in case more than k elements were added
};

module.exports = getTopKFrequentElements;

// getTopKFrequentElements([1, 1, 1, 2, 2, 3], 2);
// getTopKFrequentElements([8, 8, 8, 9, 9, 10, 10, 6, 6, 6, 6, 6, 7], 2);

"""
