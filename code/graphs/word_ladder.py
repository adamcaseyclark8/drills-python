import string
from collections import deque


def word_ladder_length(begin, end, words):
    word_set = set(words)
    if end not in word_set:
        return 0

    queue = deque([(begin, 1)])  # (current_word, steps)

    while queue:
        word, steps = queue.popleft()

        if word == end:
            return steps

        for i in range(len(word)):
            for char in string.ascii_lowercase:
                next_word = word[:i] + char + word[i + 1:]

                if next_word in word_set:
                    queue.append((next_word, steps + 1))
                    word_set.remove(next_word)  # mark as visited

    return 0  # no path found
