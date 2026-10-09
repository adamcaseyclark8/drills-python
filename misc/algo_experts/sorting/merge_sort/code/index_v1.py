def merge_sort(array):
    if len(array) <= 1:
        return array

    middle_idx = len(array) // 2
    left_half = array[:middle_idx]
    right_half = array[middle_idx:]
    return merge_sorted_arrays(merge_sort(left_half), merge_sort(right_half))


def merge_sorted_arrays(left_half, right_half):
    sorted_array = []

    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
    while i < len(left_half):
        sorted_array.append(left_half[i])
        i += 1
    while j < len(right_half):
        sorted_array.append(right_half[j])
        j += 1
    return sorted_array


if __name__ == '__main__':
    print(merge_sort([3, 4, 5, 2, 3, 1]))
