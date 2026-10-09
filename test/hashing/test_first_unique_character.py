from code.hashing.first_unique_character import find_first_unique_character


def test_finds_first_unique_in_basic_string():
    assert find_first_unique_character('leetcode') == 0


def test_finds_unique_not_at_start():
    assert find_first_unique_character('loveleetcode') == 2


def test_returns_minus_1_if_no_unique_char():
    assert find_first_unique_character('aabb') == -1


def test_handles_single_character():
    assert find_first_unique_character('z') == 0


def test_handles_repeated_single_character():
    assert find_first_unique_character('zzzz') == -1


def test_works_with_mixed_case_case_sensitive():
    assert find_first_unique_character('aA') == 0  # 'a' != 'A'


def test_works_with_spaces_and_symbols():
    # string: [space, space, !, !, a, b, a, c]
    # indices: 0,1,2,3,4,5,6,7  => 'b' at index 5 is first unique
    assert find_first_unique_character('  !!abac') == 5


def test_returns_minus_1_for_empty_string():
    assert find_first_unique_character('') == -1


def test_handles_all_unique_chars():
    assert find_first_unique_character('abcdef') == 0


def test_first_unique_in_long_string():
    # 'aabbccddeefggh' -> f at index 10 is first unique
    assert find_first_unique_character('aabbccddeefggh') == 10
