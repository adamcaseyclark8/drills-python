def array_contains_duplicates(arr):
    seen = {}
    for value in arr:
        if seen.get(value):
            return True
        seen[value] = True
    return False
