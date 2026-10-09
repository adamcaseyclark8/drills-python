from code.math.glider_find_prime_numbers import is_number_prime

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97


def test_i():
    assert is_number_prime(13) == 'Yes'


def test_ii():
    assert is_number_prime(11) == 'Yes'


def test_iii():
    assert is_number_prime(2) == 'Yes'


def test_iv():
    assert is_number_prime(97) == 'Yes'


def test_vi():
    assert is_number_prime(10) == 'No'


def test_vii():
    assert is_number_prime(100) == 'No'


def test_viii():
    assert is_number_prime(55) == 'No'
