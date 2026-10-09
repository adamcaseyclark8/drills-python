import time

from code.hashing.longest_sequence_of_numbers import longest_sequence_of_numbers


def test_has_duplicated_numbers():
    assert longest_sequence_of_numbers([100, 4, 4, 200, 1, 3, 2]) == 4


def test_handles_large_number_of_duplicates_efficiently():
    # THIS TEST WILL FAIL IF SET IS NOT USED

    array_of_numbers = [1] * 50000 + [2, 3, 4]

    start = time.perf_counter()
    results = longest_sequence_of_numbers(array_of_numbers)
    elapsed = time.perf_counter() - start

    assert results == 4
    assert elapsed < 0.1


def test_size_4_sequence():
    assert longest_sequence_of_numbers([100, 4, 200, 1, 3, 2]) == 4


def test_3_separate_sequences_of_2():
    assert longest_sequence_of_numbers([200, 199, 100, 99, 3, 2]) == 2


def test_empty_array():
    assert longest_sequence_of_numbers([]) == 0


def test_one_number_sequence():
    assert longest_sequence_of_numbers([4]) == 1


def test_two_number_sequence():
    assert longest_sequence_of_numbers([1, 2]) == 2


def test_size_5_sequence():
    assert longest_sequence_of_numbers([100, 5, 4, 200, 1, 3, 2]) == 5
