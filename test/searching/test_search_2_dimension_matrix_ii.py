from code.searching.search_2_dimension_matrix_ii import search_2d_matrix


def test_returns_true_when_target_exists_in_matrix():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
    ]
    assert search_2d_matrix(matrix, 3) is True
    assert search_2d_matrix(matrix, 16) is True
    assert search_2d_matrix(matrix, 50) is True


def test_returns_false_when_target_does_not_exist():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
    ]
    assert search_2d_matrix(matrix, 13) is False
    assert search_2d_matrix(matrix, 0) is False
    assert search_2d_matrix(matrix, 51) is False


def test_handles_empty_matrix():
    assert search_2d_matrix([], 1) is False
    assert search_2d_matrix([[]], 1) is False


def test_handles_single_row_matrix():
    matrix = [[1, 2, 3, 4, 5]]
    assert search_2d_matrix(matrix, 3) is True
    assert search_2d_matrix(matrix, 6) is False


def test_handles_single_column_matrix():
    matrix = [[1], [3], [5], [7]]
    assert search_2d_matrix(matrix, 5) is True
    assert search_2d_matrix(matrix, 2) is False


def test_handles_1x1_matrix():
    assert search_2d_matrix([[1]], 1) is True
    assert search_2d_matrix([[1]], 2) is False


def test_handles_negative_numbers():
    matrix = [
        [-10, -5, -1],
        [0, 3, 7],
        [10, 12, 15],
    ]
    assert search_2d_matrix(matrix, -5) is True
    assert search_2d_matrix(matrix, 12) is True
    assert search_2d_matrix(matrix, -6) is False
