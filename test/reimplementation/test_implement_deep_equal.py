from code.reimplementation.implement_deep_equal import implement_deep_equals_comparison


def test_compare_two_of_the_same_numbers():
    assert implement_deep_equals_comparison(5, 5) is True


def test_compare_two_different_numbers():
    assert implement_deep_equals_comparison(5, 10) is False


def test_compare_two_of_the_same_strings():
    assert implement_deep_equals_comparison('hello', 'hello') is True


def test_compare_two_different_strings():
    assert implement_deep_equals_comparison('hello', 'world') is False


def test_compare_the_same_booleans():
    assert implement_deep_equals_comparison(True, True) is True


def test_compare_different_booleans():
    assert implement_deep_equals_comparison(True, False) is False


def test_comparing_none_values():
    assert implement_deep_equals_comparison(None, None) is True


def test_comparing_none_with_not_none_values():
    assert implement_deep_equals_comparison(None, 'hello') is False
    assert implement_deep_equals_comparison(None, 3) is False
    assert implement_deep_equals_comparison(None, True) is False


def test_compare_identical_arrays():
    assert implement_deep_equals_comparison([1, 2, 3], [1, 2, 3]) is True


def test_compare_different_lengths_arrays():
    assert implement_deep_equals_comparison([1, 2, 3], [1, 2]) is False


def test_compare_same_length_arrays_with_diff_values():
    assert implement_deep_equals_comparison([1, 2, 3], [1, 2, 4]) is False


def test_compare_nested_arrays():
    first_nested_arrays = [[[1, 2], [3, 4]], [5, 6], [7, 8]]
    second_nested_arrays = [[[1, 2], [3, 4]], [5, 6], [7, 8]]

    assert implement_deep_equals_comparison(first_nested_arrays, second_nested_arrays) is True


def test_compare_2_identical_objects():
    assert implement_deep_equals_comparison({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) is True
