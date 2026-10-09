from code.sliding_window.chunk_array_into_groups import chunk_array_into_groups


def test_chunks_evenly_divisible_array():
    assert chunk_array_into_groups([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunks_with_remainder():
    assert chunk_array_into_groups([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_size_of_1():
    assert chunk_array_into_groups([1, 2, 3], 1) == [[1], [2], [3]]


def test_chunk_size_larger_than_array():
    assert chunk_array_into_groups([1, 2, 3], 5) == [[1, 2, 3]]


def test_empty_array():
    assert chunk_array_into_groups([], 2) == []


def test_chunk_size_equal_to_array_length():
    assert chunk_array_into_groups([1, 2, 3], 3) == [[1, 2, 3]]
