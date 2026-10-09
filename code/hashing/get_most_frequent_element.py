def get_most_frequent_element(array):
    counts = {}
    for item in array:
        counts[item] = counts.get(item, 0) + 1
    # max() keeps the first entry on ties, and dicts preserve insertion order
    return max(counts.items(), key=lambda entry: entry[1])[0]
