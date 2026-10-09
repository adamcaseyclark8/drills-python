def verify_valid_anagram(first, second):
    if len(first) != len(second):
        return False
    hash_table = {}

    for char in first:
        hash_table[char] = hash_table.get(char, 0) + 1

    for char in second:
        if not hash_table.get(char):
            return False
        hash_table[char] -= 1

    return True
