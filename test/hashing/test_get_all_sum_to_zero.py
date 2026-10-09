from code.hashing.get_all_sum_to_zero import get_all_pairs_that_sum_to_zero


def test_returns_pairs_that_sum_to_zero():
    assert get_all_pairs_that_sum_to_zero([-3, -1, 0, 1, 2, 3]) == [[-1, 1], [-3, 3]]


def test_returns_empty_array_when_no_pairs_sum_to_zero():
    assert get_all_pairs_that_sum_to_zero([1, 2, 3]) == []


def test_returns_empty_array_for_empty_input():
    assert get_all_pairs_that_sum_to_zero([]) == []


def test_handles_multiple_pairs():
    assert get_all_pairs_that_sum_to_zero([-2, -1, 1, 2]) == [[-1, 1], [-2, 2]]


def test_returns_empty_when_no_negatives_present():
    assert get_all_pairs_that_sum_to_zero([1, 2, 3, 4]) == []
