from code.hashing.two_number_sum_map import two_number_sum_using_map

# RETURN INDICES OF NUMBERS (NOT NUMBERS)
# ONLY RETURNS FIRST PAIR OF MATCHES
# USES A HASHMAP DATA STRUCTURE


def test_returns_indices_of_two_numbers_that_add_to_target():
    assert two_number_sum_using_map([2, 7, 11, 15], 9) == [0, 1]


def test_target_pair_is_not_at_the_start():
    assert two_number_sum_using_map([3, 2, 4], 6) == [1, 2]


def test_duplicate_values():
    assert two_number_sum_using_map([3, 3], 6) == [0, 1]


def test_negative_numbers():
    assert two_number_sum_using_map([-3, 4, 3, 90], 0) == [0, 2]


def test_negative_target():
    assert two_number_sum_using_map([-1, -2, -3, -4], -6) == [1, 3]


def test_larger_array_pair_near_the_end():
    assert two_number_sum_using_map([1, 5, 3, 8, 2, 7], 9) == [0, 3]


def test_zero_as_one_of_the_values():
    assert two_number_sum_using_map([0, 4, 3, 0], 0) == [0, 3]
