from code.hashing.find_all_duplicates import find_all_duplicates

# RETURNS NUMBER DUPLICATED (NOT THE INDEX OF DUPLICATES)
# RETURNS EMPTY ARRAY IF NO DUPLICATES


def test_returns_duplicates_from_standard_case():
    assert find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test_returns_empty_array_when_no_duplicates():
    assert find_all_duplicates([1, 2, 3, 4]) == []


def test_returns_all_elements_when_all_are_duplicates():
    assert find_all_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]


def test_returns_single_duplicate():
    assert find_all_duplicates([1, 2, 3, 2]) == [2]


def test_returns_empty_array_for_single_element():
    assert find_all_duplicates([5]) == []


def test_returns_empty_array_for_empty_input():
    assert find_all_duplicates([]) == []


def test_handles_duplicate_at_start_of_array():
    assert find_all_duplicates([3, 3, 1, 2]) == [3]
