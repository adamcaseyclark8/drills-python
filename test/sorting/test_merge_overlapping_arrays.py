from code.sorting.merge_overlapping_arrays import merge_overlapping_arrays


def test_one_overlapping_scenario():
    assert merge_overlapping_arrays([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_two_overlapping_scenarios():
    assert merge_overlapping_arrays([[1, 4], [2, 5], [3, 6], [7, 9]]) == [[1, 6], [7, 9]]


def test_duplicated_start_and_finish():
    assert merge_overlapping_arrays([[1, 3], [5, 5], [2, 6], [7, 9]]) == [[1, 6], [7, 9]]


def test_duplicated_duplicated_start_and_finish():
    assert merge_overlapping_arrays([[1, 3], [5, 5], [5, 5], [2, 6], [7, 9]]) == [[1, 6], [7, 9]]


def test_another_with_no_overlaps():
    assert merge_overlapping_arrays([[1, 3], [5, 5]]) == [[1, 3], [5, 5]]


def test_no_overlapping_arrays():
    assert merge_overlapping_arrays([[1, 3], [4, 6], [7, 9], [10, 11]]) == [[1, 3], [4, 6], [7, 9], [10, 11]]


def test_empty_array():
    assert merge_overlapping_arrays([]) == []


def test_single_nested_array():
    assert merge_overlapping_arrays([1, 2]) == [1, 2]
