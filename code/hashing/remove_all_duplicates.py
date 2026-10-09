def remove_all_duplicates(array):
    seen = {}
    result = []

    for item in array:
        if not seen.get(item):
            seen[item] = True
            result.append(item)

    return result
