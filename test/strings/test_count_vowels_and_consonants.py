from code.strings.count_vowels_and_consonants import count_vowels_and_consonants


class TestBasicCases:
    def test_hello(self):
        assert count_vowels_and_consonants('hello') == {'vowels': 2, 'consonants': 3}

    def test_javascript(self):
        assert count_vowels_and_consonants('javascript') == {'vowels': 3, 'consonants': 7}

    def test_aeiou(self):
        assert count_vowels_and_consonants('aeiou') == {'vowels': 5, 'consonants': 0}

    def test_rhythm(self):
        assert count_vowels_and_consonants('rhythm') == {'vowels': 0, 'consonants': 6}


class TestCaseInsensitivity:
    def test_upper_hello(self):
        assert count_vowels_and_consonants('HELLO') == {'vowels': 2, 'consonants': 3}

    def test_mixed_case_javascript(self):
        assert count_vowels_and_consonants('JavaScript') == {'vowels': 3, 'consonants': 7}


class TestNonLetterCharactersAreIgnored:
    def test_spaces_ignored(self):
        assert count_vowels_and_consonants('hello world') == {'vowels': 3, 'consonants': 7}

    def test_numbers_and_symbols_ignored(self):
        assert count_vowels_and_consonants('h3ll0!') == {'vowels': 0, 'consonants': 3}

    def test_only_letters_counted(self):
        assert count_vowels_and_consonants('a1b2c3') == {'vowels': 1, 'consonants': 2}


class TestEdgeCases:
    def test_empty_string(self):
        assert count_vowels_and_consonants('') == {'vowels': 0, 'consonants': 0}

    def test_string_with_only_spaces(self):
        assert count_vowels_and_consonants('   ') == {'vowels': 0, 'consonants': 0}

    def test_single_vowel(self):
        assert count_vowels_and_consonants('a') == {'vowels': 1, 'consonants': 0}

    def test_single_consonant(self):
        assert count_vowels_and_consonants('b') == {'vowels': 0, 'consonants': 1}
