from code.sliding_window.longest_unique_substring import longest_unique_substring


def test_standard_scenario():
    assert longest_unique_substring('geeksforgeeks') == 'eksforg'


def test_repeating_exact_same_twice():
    assert longest_unique_substring('abcabcbb') == 'abc'


def test_same_character_repeated():
    assert longest_unique_substring('bbbbb') == 'b'


def test_will_not_be_pwke_will_be_wke():
    assert longest_unique_substring('pwwkew') == 'wke'


def test_all_unique():
    assert longest_unique_substring('abcdef') == 'abcdef'


def test_all_same_characters():
    assert longest_unique_substring('aaaa') == 'a'


def test_empty_string():
    assert longest_unique_substring('') == ''


def test_single_character():
    assert longest_unique_substring('a') == 'a'


def test_unique_at_end():
    assert longest_unique_substring('aabcd') == 'abcd'
