def rotate_array_in_place(numbers, change):
    if not isinstance(change, int) or isinstance(change, bool) or change < 0:
        raise ValueError('change must be an positive integer')

    if change == 0:
        return numbers

    if len(numbers) == 0:
        return []

    k = change % len(numbers)

    def reverse(left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    reverse(0, len(numbers) - 1, numbers)
    reverse(0, k - 1, numbers)
    reverse(k, len(numbers) - 1, numbers)

    return numbers


# print(rotate_array_in_place([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3))
