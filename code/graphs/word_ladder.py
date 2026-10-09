r"""TODO: port to Python.

Original JavaScript (code/graphs/word-ladder.js):

const wordLadderLength = (begin, end, list) => {
    const wordSet = new Set(list);
    if (!wordSet.has(end)) return 0;

    const queue = [[begin, 1]]; // [currentWord, steps]

    while (queue.length > 0) {
        const [word, steps] = queue.shift();

        if (word === end) return steps;

        for (let i = 0; i < word.length; i++) {
            for (let c = 97; c <= 122; c++) {
                // 'a' to 'z'
                const char = String.fromCharCode(c);
                const nextWord = word.slice(0, i) + char + word.slice(i + 1);

                if (wordSet.has(nextWord)) {
                    queue.push([nextWord, steps + 1]);
                    wordSet.delete(nextWord); // mark as visited
                }
            }
        }
    }

    return 0; // no path found
};

module.exports = wordLadderLength;

"""
