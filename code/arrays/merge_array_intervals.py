def merge_array_intervals(arrays):
    if len(arrays) <= 1:
        return arrays

    # [[1,3],[2,6],[8,10],[15,18]]

    arrays.sort(key=lambda interval: interval[0])
    result = [arrays[0]]

    for i in range(1, len(arrays)):
        last = result[-1]
        current = arrays[i]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)

    return result
