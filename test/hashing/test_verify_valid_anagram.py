from code.hashing.verify_valid_anagram import verify_valid_anagram


def test_scenario_with_valid_anagram():
    assert verify_valid_anagram('cinema', 'iceman') is True


def test_not_a_valid_anagram():
    assert verify_valid_anagram('cinema', 'icemen') is False


def test_unequal_strings():
    assert verify_valid_anagram('cinema', 'icemann') is False


def test_another_variation_of_false():
    assert verify_valid_anagram('cinemaa', 'icemann') is False
