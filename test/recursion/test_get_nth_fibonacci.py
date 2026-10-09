from code.recursion.get_nth_fibonacci import get_nth_fibonacci


def test_1st_fibonacci():
    assert get_nth_fibonacci(1) == 0


def test_2nd_fibonacci():
    assert get_nth_fibonacci(2) == 1


def test_3rd_fibonacci():
    assert get_nth_fibonacci(3) == 1


def test_6th_fibonacci():
    assert get_nth_fibonacci(6) == 5


def test_10th_fibonacci():
    assert get_nth_fibonacci(10) == 34


def test_20th_fibonacci():
    assert get_nth_fibonacci(20) == 4181
