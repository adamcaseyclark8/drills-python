from code.greedy.perform_column_addition import perform_column_addition


def test_456_plus_77_returns_533():
    assert perform_column_addition('456', '77') == '533'


def test_11_plus_123_returns_134():
    assert perform_column_addition('11', '123') == '134'


def test_999_plus_1_returns_1000():
    assert perform_column_addition('999', '1') == '1000'


def test_0_plus_0_returns_0():
    assert perform_column_addition('0', '0') == '0'


def test_same_length_no_carry():
    assert perform_column_addition('123', '456') == '579'


def test_large_numbers():
    assert perform_column_addition('9999999999', '1') == '10000000000'


def test_single_digits_with_carry():
    assert perform_column_addition('9', '9') == '18'


def test_one_number_is_zero():
    assert perform_column_addition('500', '0') == '500'
