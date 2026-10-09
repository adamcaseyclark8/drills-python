from code.dynamic_programming.longest_common_subsequence import longest_common_subsequence


def test_abcde_and_ace_returns_3():
    assert longest_common_subsequence('abcde', 'ace') == 3


def test_abc_and_abc_returns_3():
    assert longest_common_subsequence('abc', 'abc') == 3


def test_abc_and_def_returns_0():
    assert longest_common_subsequence('abc', 'def') == 0


def test_empty_strings_returns_0():
    assert longest_common_subsequence('', '') == 0


def test_one_empty_string_returns_0():
    assert longest_common_subsequence('abc', '') == 0


def test_single_matching_char_returns_1():
    assert longest_common_subsequence('a', 'a') == 1


def test_single_non_matching_char_returns_0():
    assert longest_common_subsequence('a', 'b') == 0


def test_bsbininm_and_jmjkbkjkv_returns_1():
    assert longest_common_subsequence('bsbininm', 'jmjkbkjkv') == 1
