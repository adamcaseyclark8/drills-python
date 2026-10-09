from code.arrays.filter_all_prime_numbers import filter_all_prime_numbers

PRIMES_UNDER_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def test_1_thru_100():
    assert filter_all_prime_numbers(list(range(1, 101))) == PRIMES_UNDER_100


def test_basic_case():
    assert filter_all_prime_numbers([1, 2, 3, 4, 5, 6, 7]) == [2, 3, 5, 7]


def test_no_primes():
    assert filter_all_prime_numbers([1, 4, 6, 8, 9]) == []


def test_all_primes():
    assert filter_all_prime_numbers([2, 3, 5, 7, 11]) == [2, 3, 5, 7, 11]


def test_empty_array():
    assert filter_all_prime_numbers([]) == []


def test_negative_numbers():
    assert filter_all_prime_numbers([-3, -1, 0, 1, 2]) == [2]


def test_large_prime():
    assert filter_all_prime_numbers([97, 98, 99, 100]) == [97]
