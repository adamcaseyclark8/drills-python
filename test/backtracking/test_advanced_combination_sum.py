from code.backtracking.advanced_combination_sum import perform_advanced_combination_sum

# CANDIDATES MAY HAVE DUPLICATES
# EACH NUMBER USED ONCE ONLY
# NO DUPLICATE COMBINATIONS IN OUTPUT


def test_basic_case_with_duplicates_in_input():
    result = perform_advanced_combination_sum([10, 1, 2, 7, 6, 1, 5], 8)
    assert len(result) == 4
    assert [1, 1, 6] in result
    assert [1, 2, 5] in result
    assert [1, 7] in result
    assert [2, 6] in result


def test_no_valid_combination():
    assert perform_advanced_combination_sum([2, 4], 3) == []


def test_no_duplicate_combinations_in_output():
    result = perform_advanced_combination_sum([1, 1, 1, 1], 2)
    assert len(result) == 1
    assert [1, 1] in result


def test_single_element_equals_target():
    result = perform_advanced_combination_sum([1, 2, 3], 3)
    assert len(result) == 2
    assert [3] in result
    assert [1, 2] in result


def test_each_element_used_at_most_once():
    result = perform_advanced_combination_sum([1, 2, 3], 4)
    assert len(result) == 1
    assert [2, 2] not in result
    assert [1, 3] in result
