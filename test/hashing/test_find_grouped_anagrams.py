from code.hashing.find_grouped_anagrams import find_grouped_anagrams


def sort_grouped_anagrams(output):
    # Helper to normalize output for test comparison
    return sorted((sorted(group) for group in output), key=lambda group: group[0])


def test_groups_basic_anagrams_together():
    expected = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
    result = find_grouped_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
    assert sort_grouped_anagrams(result) == sort_grouped_anagrams(expected)


def test_returns_empty_array_when_input_is_empty():
    assert find_grouped_anagrams([]) == []


def test_no_anagrams():
    result = find_grouped_anagrams(['cat', 'dog', 'bird'])
    for group in [['cat'], ['dog'], ['bird']]:
        assert group in result


def test_handles_single_word_input():
    assert find_grouped_anagrams(['abc']) == [['abc']]


def test_handles_all_identical_strings():
    assert find_grouped_anagrams(['aaa', 'aaa', 'aaa']) == [['aaa', 'aaa', 'aaa']]


def test_all_same_anagram_group():
    result = find_grouped_anagrams(['abc', 'bca', 'cab'])
    assert len(result) == 1
    assert sorted(result[0]) == ['abc', 'bca', 'cab']


def test_treats_words_with_different_lengths_as_non_anagrams():
    expected = [['ab'], ['abc'], ['a']]
    assert sort_grouped_anagrams(find_grouped_anagrams(['ab', 'abc', 'a'])) == sort_grouped_anagrams(expected)


def test_handles_mix_of_anagrams_and_non_anagrams():
    words = ['listen', 'silent', 'enlist', 'google', 'gooegl', 'abc']
    expected = [['abc'], ['enlist', 'listen', 'silent'], ['google', 'gooegl']]
    assert sort_grouped_anagrams(find_grouped_anagrams(words)) == sort_grouped_anagrams(expected)
