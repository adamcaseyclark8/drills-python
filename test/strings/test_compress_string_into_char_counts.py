from code.strings.compress_string_into_char_counts import compress_string_into_char_counts


class TestBasicCompression:
    def test_compresses_repeated_characters(self):
        assert compress_string_into_char_counts('aabcccdddd') == 'a2b1c3d4'

    def test_compresses_all_same_characters(self):
        assert compress_string_into_char_counts('aaaaaaa') == 'a7'

    def test_compresses_two_groups(self):
        assert compress_string_into_char_counts('aaabbb') == 'a3b3'


class TestNoCompressionNeeded:
    def test_returns_original_if_compressed_is_not_smaller(self):
        assert compress_string_into_char_counts('aabbcc') == 'aabbcc'

    def test_returns_original_if_all_characters_are_unique(self):
        assert compress_string_into_char_counts('abcd') == 'abcd'


class TestEdgeCases:
    def test_returns_empty_string_for_empty_input(self):
        assert compress_string_into_char_counts('') == ''

    def test_returns_none_for_none_input(self):
        assert compress_string_into_char_counts(None) is None

    def test_handles_single_character(self):
        assert compress_string_into_char_counts('a') == 'a'

    def test_handles_single_repeated_character(self):
        assert compress_string_into_char_counts('aa') == 'aa'
