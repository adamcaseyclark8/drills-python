from code.two_pointers.three_number_sum import three_number_sum


def test_example_with_1_triplet():
    assert three_number_sum([1, 4, 45, 6, 10, 8], 13) == [[1, 4, 8]]


def test_example_with_2_triplets():
    assert three_number_sum([-1, 0, 1, 2, -1, -4], 0) == [[-1, -1, 2], [-1, 0, 1]]
