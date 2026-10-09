def flatten_nested_list(arr):
    result = []

    def flatten(items):
        for item in items:
            if isinstance(item, list):
                flatten(item)
            else:
                result.append(item)

    flatten(arr)
    return result
