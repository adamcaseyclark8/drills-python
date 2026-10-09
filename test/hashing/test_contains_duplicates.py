from code.hashing.contains_duplicates import array_contains_duplicates


def test_i_numbers():
    assert array_contains_duplicates([1, 2, 2, 3, 4, 4, 5]) is True


def test_ii_strings():
    assert array_contains_duplicates(['a', 'b', 'a', 'c', 'b']) is True


def test_iii_false():
    assert array_contains_duplicates([10, 20, 30]) is False


def test_returns_false_when_input_is_empty():
    assert array_contains_duplicates([]) is False


def test_returns_false_when_only_one_element():
    assert array_contains_duplicates([1]) is False


# my test cases above - chatgpt below
def test_returns_false_when_all_elements_are_unique():
    assert array_contains_duplicates([1, 2, 3, 4]) is False


def test_returns_true_when_duplicates_exist():
    assert array_contains_duplicates([1, 2, 3, 2]) is True


def test_returns_true_when_all_elements_are_the_same():
    assert array_contains_duplicates([5, 5, 5, 5]) is True


def test_works_with_strings():
    assert array_contains_duplicates(['a', 'b', 'c', 'a']) is True
    assert array_contains_duplicates(['x', 'y', 'z']) is False


def test_works_with_mixed_types_number_vs_string():
    assert array_contains_duplicates([1, '1']) is False  # different types
