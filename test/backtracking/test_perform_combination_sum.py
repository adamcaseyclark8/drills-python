from code.backtracking.perform_combination_sum import perform_combination_sum


def test_returns_correct_combinations_for_2_3_6_7_target_7():
    result = perform_combination_sum([2, 3, 6, 7], 7)
    assert [2, 2, 3] in result
    assert [7] in result
    assert len(result) == 2


def test_returns_correct_combinations_for_2_3_5_target_8():
    result = perform_combination_sum([2, 3, 5], 8)
    assert [2, 2, 2, 2] in result
    assert [2, 3, 3] in result
    assert [3, 5] in result
    assert len(result) == 3


def test_returns_empty_when_no_combination_exists():
    assert perform_combination_sum([3, 5], 1) == []


def test_single_candidate_that_equals_target():
    assert perform_combination_sum([7], 7) == [[7]]


def test_candidate_can_be_reused_multiple_times():
    assert perform_combination_sum([2], 6) == [[2, 2, 2]]
