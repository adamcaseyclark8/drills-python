from code.arrays.rotate_array_in_place import rotate_array_in_place

# MOVE START OF INDEX BACKWARDS IN ARRAY
# CHANGE IS 3 => START GOES FROM INDEX 0 TO INDEX 3
#
# RULES:
# 1.) CHANGE HAS TO BE NUMBER
# 2.) CHANGE HAS TO BE GREATER THAN ZERO
# 3.) MUST HANDLE NULL AND EMPTY ARRAY


def test_basic_case_k_3():
    assert rotate_array_in_place([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]


def test_k_1_shifts_everything_one_step_right():
    assert rotate_array_in_place([1, 2, 3], 1) == [3, 1, 2]


def test_k_equals_array_length_back_to_original():
    assert rotate_array_in_place([1, 2, 3, 4], 4) == [1, 2, 3, 4]


def test_k_larger_than_array_length_wraps_around():
    assert rotate_array_in_place([1, 2, 3, 4, 5, 6, 7], 10) == [5, 6, 7, 1, 2, 3, 4]


def test_k_0_no_change():
    assert rotate_array_in_place([1, 2, 3], 0) == [1, 2, 3]


def test_single_element_array():
    assert rotate_array_in_place([1], 5) == [1]


def test_two_element_array():
    assert rotate_array_in_place([1, 2], 1) == [2, 1]


def test_all_same_values():
    assert rotate_array_in_place([3, 3, 3, 3], 2) == [3, 3, 3, 3]
