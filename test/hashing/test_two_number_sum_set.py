from code.hashing.two_number_sum_set import two_number_sum_using_set

# RETURN NUMBERS (NOT INDICES)
# RETURNS ALL PAIRS OF MATCHES
# USES A SET DATA STRUCTURE


def test_returns_pair_of_numbers_that_sum_to_target_simple_case():
    assert two_number_sum_using_set([3, 5, -4, 8, 11, 1, -1, 6], 10) == [[11, -1]]


def test_returns_pair_when_numbers_are_at_the_start_end_of_the_array():
    assert two_number_sum_using_set([1, 2, 3, 8, 5], 6) == [[1, 5]]


def test_returns_empty_array_when_no_two_numbers_sum_to_target():
    assert two_number_sum_using_set([1, 2, 3, 4], 100) == []


def test_handles_negative_numbers_correctly():
    assert two_number_sum_using_set([-3, -1, -5, -4], -5) == [[-1, -4]]


def test_returns_every_valid_pair_when_multiple_are_possible():
    result = two_number_sum_using_set([2, 4, 6, 8], 10)
    assert sorted(result) == sorted([[4, 6], [2, 8]])


def test_returns_empty_array_when_input_array_is_empty():
    assert two_number_sum_using_set([], 10) == []


def test_returns_empty_array_when_array_has_only_one_element():
    assert two_number_sum_using_set([10], 10) == []


def test_returns_correct_result_with_duplicate_numbers():
    assert two_number_sum_using_set([5, 5, 3], 10) == [[5, 5]]


def test_does_not_use_the_same_element_twice():
    assert two_number_sum_using_set([5], 10) == []


def test_3_matches():
    result = two_number_sum_using_set([1, 2, 3, 4, 5, 6, 7], 8)
    assert sorted(result) == sorted([[1, 7], [2, 6], [3, 5]])
