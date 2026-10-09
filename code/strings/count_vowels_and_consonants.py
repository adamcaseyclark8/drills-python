r"""TODO: port to Python.

Original JavaScript (code/strings/count-vowels-and-consonants.js):

const countVowelsAndConsonants = str => {
    const lower = str.toLowerCase();
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);

    let vowelCount = 0;
    let consonantCount = 0;

    for (const char of lower) {
        if (char >= 'a' && char <= 'z') {
            if (vowels.has(char)) {
                vowelCount++;
            } else {
                consonantCount++;
            }
        }
    }

    return { vowels: vowelCount, consonants: consonantCount };
};

module.exports = countVowelsAndConsonants;

"""
