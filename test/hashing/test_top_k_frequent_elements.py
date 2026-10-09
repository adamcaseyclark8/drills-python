from code.hashing.top_k_frequent_elements import get_top_k_frequent_elements


def test_returns_top_2_frequent_elements_from_a_simple_array():
    assert sorted(get_top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2)) == [1, 2]


def test_returns_the_only_element_when_k_is_1():
    assert get_top_k_frequent_elements([4, 4, 4, 4], 1) == [4]


def test_returns_all_unique_elements_when_k_equals_number_of_unique_elements():
    assert sorted(get_top_k_frequent_elements([1, 2, 3, 4], 4)) == [1, 2, 3, 4]


def test_returns_element_with_highest_frequency_from_array_with_mixed_frequencies():
    assert get_top_k_frequent_elements([5, 3, 1, 1, 1, 3, 5, 5, 5], 1) == [5]


def test_handles_negative_numbers_and_returns_top_k():
    assert sorted(get_top_k_frequent_elements([-1, -1, -2, -2, -2, 3], 2)) == [-2, -1]


def test_handles_case_where_multiple_elements_have_the_same_frequency():
    result = get_top_k_frequent_elements([1, 2, 3, 4], 2)
    assert len(result) == 2
    assert set(result) <= {1, 2, 3, 4}  # any 2 out of 4
