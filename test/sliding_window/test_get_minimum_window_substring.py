from code.sliding_window.get_minimum_window_substring import get_minimum_window_substring


def test_adobecodebanc_and_abc_returns_banc():
    assert get_minimum_window_substring('ADOBECODEBANC', 'ABC') == 'BANC'


def test_a_and_a_returns_a():
    assert get_minimum_window_substring('a', 'a') == 'a'


def test_a_and_b_returns_empty_string():
    assert get_minimum_window_substring('a', 'b') == ''


def test_empty_s_returns_empty_string():
    assert get_minimum_window_substring('', 'a') == ''


def test_empty_t_returns_empty_string():
    assert get_minimum_window_substring('abc', '') == ''


def test_t_longer_than_s_returns_empty_string():
    assert get_minimum_window_substring('ab', 'abc') == ''


def test_duplicate_chars_in_t():
    assert get_minimum_window_substring('aab', 'aa') == 'aa'


def test_exact_match_returns_full_string():
    assert get_minimum_window_substring('abc', 'abc') == 'abc'


def test_multiple_valid_windows_returns_smallest():
    assert get_minimum_window_substring('cabwefgewcwaefgcf', 'cae') == 'cwae'
