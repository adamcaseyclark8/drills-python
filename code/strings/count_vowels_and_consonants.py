def count_vowels_and_consonants(string):
    lower = string.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}

    vowel_count = 0
    consonant_count = 0

    for char in lower:
        if 'a' <= char <= 'z':
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return {'vowels': vowel_count, 'consonants': consonant_count}
