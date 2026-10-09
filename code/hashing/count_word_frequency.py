def count_word_frequency(sentence):
    if not sentence or len(sentence.strip()) == 0:
        return {}

    counts = {}
    words = sentence.lower().split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts
