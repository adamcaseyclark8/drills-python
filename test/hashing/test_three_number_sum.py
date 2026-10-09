from code.hashing.three_number_sum import three_number_sum


def test_an_array_with_less_than_3_numbers_returns_false():
    assert three_number_sum([3, 6], 9) is False


def test_3_numbers_that_does_not_add_up_does_not_work():
    assert three_number_sum([1, 2, 3], 7) is False


def test_4_numbers_that_sums_to_target_returns_false():
    assert three_number_sum([1, 2, 3, 4], 10) is False


def test_three_numbers_works():
    assert three_number_sum([3, 5, 1], 9) is True


def test_array_can_include_zero():
    assert three_number_sum([3, 6, 0], 9) is True


def test_duplicated_numbers_in_the_array_works():
    assert three_number_sum([3, 6, 0, 3], 9) is True


def test_negative_numbers_after_passing_works():
    assert three_number_sum([3, 6, 0, -3], 9) is True


def test_negative_numbers_before_passing_works():
    assert three_number_sum([3, 6, -3, 0], 9) is True


def test_negative_numbers_can_be_used_in_the_total():
    assert three_number_sum([3, 9, -3], 9) is True


def test_first_number_not_included_in_the_solution():
    assert three_number_sum([7, 0, 56, 3, 6, 1], 9) is True


def test_two_correct_solutions_will_not_break():
    assert three_number_sum([7, 0, 56, 3, 6, 1, 2], 9) is True


def test_value_of_none_in_array_will_not_break():
    assert three_number_sum([None, 0, 56, 3, 6, 1, 2], 9) is True


def test_negative_target_value_works():
    assert three_number_sum([-3, -6, 1], -8) is True
