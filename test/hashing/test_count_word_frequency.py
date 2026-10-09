from code.hashing.count_word_frequency import count_word_frequency


class TestBasicCounting:
    def test_counts_single_word_occurrences(self):
        assert count_word_frequency('the cat sat on the mat the cat') == {
            'the': 3,
            'cat': 2,
            'sat': 1,
            'on': 1,
            'mat': 1,
        }

    def test_counts_single_word(self):
        assert count_word_frequency('hello') == {'hello': 1}

    def test_counts_all_unique_words(self):
        assert count_word_frequency('one two three') == {'one': 1, 'two': 1, 'three': 1}


class TestCaseInsensitivity:
    def test_treats_uppercase_and_lowercase_as_the_same_word(self):
        assert count_word_frequency('The the THE') == {'the': 3}


class TestWhitespaceHandling:
    def test_handles_multiple_spaces_between_words(self):
        assert count_word_frequency('hello   world') == {'hello': 1, 'world': 1}

    def test_handles_leading_and_trailing_spaces(self):
        assert count_word_frequency('  hello world  ') == {'hello': 1, 'world': 1}


class TestEdgeCases:
    def test_returns_empty_dict_for_empty_string(self):
        assert count_word_frequency('') == {}

    def test_returns_empty_dict_for_none(self):
        assert count_word_frequency(None) == {}

    def test_returns_empty_dict_for_whitespace_only(self):
        assert count_word_frequency('   ') == {}
