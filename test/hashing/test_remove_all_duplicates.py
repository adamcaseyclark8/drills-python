from code.hashing.remove_all_duplicates import remove_all_duplicates


def test_removes_duplicates_from_an_array_of_numbers():
    assert sorted(remove_all_duplicates([1, 2, 2, 3, 4, 4, 5])) == [1, 2, 3, 4, 5]


def test_removes_duplicates_from_an_array_of_strings():
    assert sorted(remove_all_duplicates(['a', 'b', 'a', 'c', 'b'])) == ['a', 'b', 'c']


def test_returns_same_array_when_no_duplicates_exist():
    assert sorted(remove_all_duplicates([10, 20, 30])) == [10, 20, 30]


def test_returns_empty_array_when_input_is_empty():
    assert remove_all_duplicates([]) == []


def test_works_with_all_elements_being_the_same():
    assert remove_all_duplicates([1, 1, 1, 1]) == [1]


def test_maintains_order_of_first_occurrence():
    assert remove_all_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']


# MY TEST CASES / ABOVE SUPPLIED BY CHATGPT
def test_multiple_element_array():
    assert remove_all_duplicates([1, 1, 2, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]


def test_one_element_array():
    assert remove_all_duplicates([1]) == [1]
