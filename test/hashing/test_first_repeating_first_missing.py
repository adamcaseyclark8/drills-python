from code.hashing.first_repeating_first_missing import first_repeating_first_missing

# HANDLES ARRAY WITH ONE ELEMENT
# HANDLES NO REPEATING ELEMENT
# HANDLES NO MISSING ELEMENT


def test_finds_first_missing_and_repeating_in_a_simple_case():
    assert first_repeating_first_missing([1, 3, 4, 5, 3]) == [3, 2]


def test_handles_array_with_repeating_first_element():
    assert first_repeating_first_missing([2, 2, 3, 4, 5]) == [2, 1]


def test_handles_missing_1():
    assert first_repeating_first_missing([2, 3, 4, 4, 5]) == [4, 1]


def test_handles_duplicate_in_middle():
    assert first_repeating_first_missing([1, 2, 2, 3, 5]) == [2, 4]


def test_works_when_last_element_repeats():
    assert first_repeating_first_missing([1, 2, 3, 5, 5]) == [5, 4]


def test_works_with_negatives_and_zeros():
    assert first_repeating_first_missing([0, -1, 1, 3, 3, 5]) == [3, 2]


def test_handles_array_with_only_one_element():
    assert first_repeating_first_missing([1]) == [-1, 2]


def test_handles_no_repeating_element():
    assert first_repeating_first_missing([1, 2, 3, 4, 5]) == [-1, 6]


def test_handles_no_missing_element_but_has_repeat():
    assert first_repeating_first_missing([1, 2, 3, 4, 4, 5]) == [4, 6]


def test_works_with_unordered_input():
    assert first_repeating_first_missing([3, 1, 4, 2, 2]) == [2, 5]
