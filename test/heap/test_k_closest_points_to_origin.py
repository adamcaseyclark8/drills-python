from code.heap.k_closest_points_to_origin import find_k_closest_points_to_origin


def test_basic_case_k_1():
    assert find_k_closest_points_to_origin([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test_basic_case_k_2():
    result = find_k_closest_points_to_origin([[3, 3], [5, -1], [-2, 4]], 2)
    assert len(result) == 2
    assert [3, 3] in result
    assert [-2, 4] in result


def test_k_equals_total_number_of_points():
    assert len(find_k_closest_points_to_origin([[1, 1], [2, 2], [3, 3]], 3)) == 3


def test_point_at_origin_is_always_closest():
    assert find_k_closest_points_to_origin([[0, 0], [1, 1], [2, 2]], 1) == [[0, 0]]


def test_negative_coordinates():
    assert [0, 1] in find_k_closest_points_to_origin([[-1, -1], [-5, -5], [0, 1]], 1)


def test_points_equidistant_returns_k_of_them():
    assert len(find_k_closest_points_to_origin([[1, 0], [0, 1], [-1, 0], [0, -1]], 2)) == 2


def test_large_k():
    assert len(find_k_closest_points_to_origin([[1, 2], [3, 4], [5, 6], [0, 1]], 4)) == 4
