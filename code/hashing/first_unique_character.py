def find_first_unique_character(string):
    freq = {}

    for char in string:
        freq[char] = freq.get(char, 0) + 1

    for i in range(len(string)):
        if freq[string[i]] == 1:
            return i

    return -1
