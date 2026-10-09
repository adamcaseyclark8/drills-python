def chunk_array_into_groups(array, size):
    results = []
    for i in range(0, len(array), size):
        results.append(array[i:i + size])
    return results
