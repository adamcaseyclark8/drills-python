def perform_binary_search(array, target):
    return perform_binary_search_helper(array, target, 0, len(array) - 1)


def perform_binary_search_helper(array, target, left, right):
    # loop through array

    while left <= right:
        middle = (left + right) // 2
        potential = array[middle]

        print(f'middle: {middle}, target: {target} vs. potential: {potential}, left: {left}, right: {right}')

        if target == potential:
            return middle
        elif target < potential:
            right = middle - 1
        else:
            left = middle + 1
    return -1
