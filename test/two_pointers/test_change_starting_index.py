import pytest

from code.two_pointers.change_starting_index import change_starting_index

# MOVE START OF INDEX FORWARDS IN ARRAY
# CHANGE IS 3 => START GOES FROM INDEX 0 TO INDEX len(ARRAY) - 3
#
# RULES:
# 1.) CHANGE HAS TO BE NUMBER
# 2.) CHANGE HAS TO BE GREATER THAN ZERO
# 3.) MUST HANDLE NULL AND EMPTY ARRAY


def test_given_test_case():
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 2) == [3, 4, 5, 6, 7, 1, 2]


def test_another_test_case():
    assert change_starting_index([7, 1, 2, 3, 4, 5, 6], 6) == [6, 7, 1, 2, 3, 4, 5]


def test_when_array_is_unordered():
    assert change_starting_index([3, 4, 5, 6, 7, 1, 2], 2) == [5, 6, 7, 1, 2, 3, 4]


def test_with_small_array():
    assert change_starting_index([1, 2], 1) == [2, 1]


def test_when_starting_index_loops_array_many_times():
    assert change_starting_index([1, 2], 8) == [1, 2]


def test_when_the_starting_index_is_zero():
    assert change_starting_index([1, 2], 0) == [1, 2]


def test_when_the_array_is_empty():
    assert change_starting_index([], 3) == []


def test_should_raise_an_error_when_negative_integer_used():
    with pytest.raises(ValueError, match='change must be an positive integer'):
        change_starting_index([1, 2, 3, 4, 5, 6, 7], -1)


def test_every_iteration():
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 1) == [2, 3, 4, 5, 6, 7, 1]
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 2) == [3, 4, 5, 6, 7, 1, 2]
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 3) == [4, 5, 6, 7, 1, 2, 3]
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 4) == [5, 6, 7, 1, 2, 3, 4]
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 5) == [6, 7, 1, 2, 3, 4, 5]
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 6) == [7, 1, 2, 3, 4, 5, 6]
    assert change_starting_index([1, 2, 3, 4, 5, 6, 7], 7) == [1, 2, 3, 4, 5, 6, 7]
