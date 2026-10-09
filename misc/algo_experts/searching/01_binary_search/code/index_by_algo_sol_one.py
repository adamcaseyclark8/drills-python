def perform_binary_search(array, target, *_):
    return perform_binary_search_helper(array, target, 0, len(array) - 1)


def perform_binary_search_helper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    potential = array[middle]

    if target == potential:
        return middle
    elif target > potential:
        return perform_binary_search(array, target, left, middle - 1)
    else:
        return perform_binary_search(array, target, middle + 1, right)


# [1,5,23,111], 11, 0, 4
# middle: 2, potential = 5
#
