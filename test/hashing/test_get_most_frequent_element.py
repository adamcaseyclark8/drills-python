from code.hashing.get_most_frequent_element import get_most_frequent_element

# THE FIRST ENCOUNTERED MOST ELEMENT IF TIED


def test_returns_most_frequent_element():
    assert get_most_frequent_element(['a', 'b', 'a', 'c', 'a', 'b']) == 'a'


def test_single_element_array():
    assert get_most_frequent_element(['x']) == 'x'


def test_all_same_elements():
    assert get_most_frequent_element(['z', 'z', 'z']) == 'z'


def test_numbers():
    assert get_most_frequent_element([1, 2, 2, 3, 2]) == 2


def test_tie_returns_first_most_frequent_encountered():
    assert get_most_frequent_element(['a', 'b', 'b', 'a']) == 'a'
