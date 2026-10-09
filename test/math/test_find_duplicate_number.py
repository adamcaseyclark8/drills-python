from code.math.find_duplicate_number import find_duplicate_number


def test_finds_a_simple_duplicate():
    assert find_duplicate_number([1, 3, 4, 2, 2]) == [2]


def test_finds_duplicate_at_beginning_and_end():
    assert find_duplicate_number([5, 4, 3, 2, 1, 5]) == [5]


def test_returns_minus_1_if_no_duplicate_edge_case():
    assert find_duplicate_number([1, 2, 3, 4]) == -1


def test_works_with_smallest_valid_array():
    assert find_duplicate_number([1, 1]) == [1]


def test_works_when_duplicate_is_the_largest_number():
    assert find_duplicate_number([1, 2, 3, 4, 5, 5]) == [5]


def test_works_when_duplicate_is_the_smallest_number():
    assert find_duplicate_number([1, 1, 2, 3, 4, 5]) == [1]


def test_handles_unordered_input():
    assert find_duplicate_number([9, 8, 7, 6, 9, 5, 4, 3, 2, 1]) == [9]
