def product_except_self(array):
    results = [1] * len(array)
    prefix = 1
    for i in range(len(array)):
        results[i] = prefix
        prefix *= array[i]
    suffix = 1
    for i in range(len(array) - 1, -1, -1):
        results[i] *= suffix
        suffix *= array[i]
    return results
