def find_grouped_anagrams(array_of_strings):
    result = {}
    for word in array_of_strings:
        cleansed = ''.join(sorted(word))
        if cleansed in result:
            result[cleansed].append(word)
        else:
            result[cleansed] = [word]
    return list(result.values())
