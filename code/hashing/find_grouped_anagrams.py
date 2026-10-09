r"""TODO: port to Python.

Original JavaScript (code/hashing/find-grouped-anagrams.js):

const findGroupedAnagrams = arrayOfStrings => {
    let result = {};
    for (let word of arrayOfStrings) {
        let cleansed = word.split('').sort().join('');
        if (result[cleansed]) {
            result[cleansed].push(word);
        } else {
            result[cleansed] = [word];
        }
    }
    return Object.values(result);
};

module.exports = findGroupedAnagrams;

"""
