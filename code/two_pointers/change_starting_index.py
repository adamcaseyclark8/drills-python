def change_starting_index(numbers, change):
    if not isinstance(change, int) or isinstance(change, bool) or change < 0:
        raise ValueError('change must be an positive integer')

    if change == 0:
        return numbers

    if len(numbers) == 0:
        return []

    last = len(numbers) - 1
    left_adjusted_index = len(numbers) - change
    new_start_location = left_adjusted_index % len(numbers)
    new_end_location = new_start_location - 1

    def reverse_array_in_place(start, end, array):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
        return array

    # entire array, beginning to new end location, new start to end
    reverse_array_in_place(0, len(numbers) - 1, numbers)
    reverse_array_in_place(0, new_end_location, numbers)
    reverse_array_in_place(new_start_location, last, numbers)

    return numbers


# print(change_starting_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
