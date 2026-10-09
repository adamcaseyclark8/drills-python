def merge_sort(array):
    if len(array) <= 1:
        return array

    auxiliary_array = array[:]
    merge_sort_helper(array, 0, len(array) - 1, auxiliary_array)
    return array


def merge_sort_helper(main_array, start_idx, end_idx, auxiliary_array):
    if start_idx == end_idx:
        return

    middle_idx = (start_idx + end_idx) // 2
    merge_sort_helper(auxiliary_array, start_idx, middle_idx, main_array)
    merge_sort_helper(auxiliary_array, middle_idx + 1, end_idx, main_array)
    do_merge(main_array, start_idx, middle_idx, end_idx, auxiliary_array)


def do_merge(main_array, start_idx, middle_idx, end_idx, auxiliary_array):
    k = start_idx
    i = start_idx
    j = middle_idx + 1

    while i <= middle_idx and j <= end_idx:
        if auxiliary_array[i] <= auxiliary_array[j]:
            main_array[k] = auxiliary_array[i]
            i += 1
        else:
            main_array[k] = auxiliary_array[j]
            j += 1
        k += 1
    while i <= middle_idx:
        main_array[k] = auxiliary_array[i]
        i += 1
        k += 1
    while j <= end_idx:
        main_array[k] = auxiliary_array[j]
        j += 1
        k += 1
