def selection_sort(array):
    start_idx = 0

    while start_idx < len(array) - 1:
        smallest_idx = start_idx

        for i in range(start_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i

        swap(start_idx, smallest_idx, array)
        start_idx += 1
    return array


def swap(first, second, array):
    array[first], array[second] = array[second], array[first]
