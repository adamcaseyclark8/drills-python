from code.two_pointers.move_zeroes_right import move_zeroes_right


def test_one_example_of_move_zeroes_right():
    assert move_zeroes_right([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_another_example_of_move_zeroes():
    assert move_zeroes_right([0, 0, 1]) == [1, 0, 0]


def test_3rd_example_of_move_zeroes():
    assert move_zeroes_right([0, 2, 0, 3, 5, 6]) == [2, 3, 5, 6, 0, 0]
