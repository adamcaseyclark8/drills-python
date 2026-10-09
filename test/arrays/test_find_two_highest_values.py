from code.arrays.find_two_highest_values import find_two_highest_values

# cannot sort the array
# must handle null or empty array
# must handle arrays with less than 2 elements
# must handle duplicate values


def test_both_numbers_are_positive():
    assert find_two_highest_values([1, 2, 3, 4, 5, 6, 7, 8]) == [8, 7]


def test_high_is_positive_second_is_negative():
    assert find_two_highest_values([1, -1, -2, -3]) == [1, -1]


def test_all_numbers_in_array_negative():
    assert find_two_highest_values([-1, -2, -3, -4, -5, -6, -7, -8]) == [-1, -2]
