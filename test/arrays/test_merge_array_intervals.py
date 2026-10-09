from code.arrays.merge_array_intervals import merge_array_intervals

# EACH INTERVAL HAS EXACTLY 2 ELEMENTS [START, END]
# START <= END ALWAYS (A VALID INTERVAL NEVER GOES BACKWARDS)
# INTERVALS CAN OVERLAP, TOUCH, OR BE COMPLETELY NESTED
# INPUT CAN BE UNSORTED
# VALUES CAN BE NEGATIVE
# ARRAY CAN BE EMPTY


def test_basic_overlapping_intervals():
    assert merge_array_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_intervals_that_touch_at_boundary():
    assert merge_array_intervals([[1, 4], [4, 5]]) == [[1, 5]]


def test_no_overlapping_intervals():
    assert merge_array_intervals([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]]


def test_all_intervals_merge_into_one():
    assert merge_array_intervals([[1, 4], [2, 5], [3, 6]]) == [[1, 6]]


def test_one_interval_completely_contains_another():
    assert merge_array_intervals([[1, 10], [2, 5]]) == [[1, 10]]


def test_unsorted_input():
    assert merge_array_intervals([[8, 10], [1, 3], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_single_interval():
    assert merge_array_intervals([[1, 5]]) == [[1, 5]]


def test_two_non_overlapping_intervals():
    assert merge_array_intervals([[1, 2], [4, 5]]) == [[1, 2], [4, 5]]
