from code.two_pointers.verify_valid_palindrome import verify_valid_palindrome

# must ignore spaces, punctuation and case
# must handle None and empty string
# must handle single character


def test_returns_true_for_a_simple_palindrome():
    assert verify_valid_palindrome('racecar') is True


def test_returns_false_for_a_non_palindrome():
    assert verify_valid_palindrome('hello') is False


def test_ignores_case():
    assert verify_valid_palindrome('RaceCar') is True


def test_ignores_non_alphanumeric_characters():
    assert verify_valid_palindrome('A man, a plan, a canal: Panama') is True


def test_returns_true_for_single_character():
    assert verify_valid_palindrome('x') is True


def test_returns_false_for_empty_string():
    assert verify_valid_palindrome('') is False


def test_returns_true_for_string_with_only_non_alphanumeric_characters():
    # technically empty after cleaning → palindrome
    assert verify_valid_palindrome('!@#$') is True


def test_handles_numeric_palindromes():
    assert verify_valid_palindrome('12321') is True
    assert verify_valid_palindrome('12345') is False


def test_long_palindrome_with_spaces_and_punctuation():
    assert verify_valid_palindrome('No lemon, no melon') is True
