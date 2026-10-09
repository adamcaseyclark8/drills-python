import pytest

from ..code.longest_range import longest_range

UNSOLVED = pytest.mark.xfail(strict=True, reason='longest_range is unfinished (fails in the JS original too)')


@UNSOLVED
def test_tc_1():
    assert longest_range([1]) == [1, 1]


@UNSOLVED
def test_tc_2():
    assert longest_range([1, 2]) == [1, 2]


@UNSOLVED
def test_tc_3():
    assert longest_range([4, 2, 1, 3]) == [1, 4]


@UNSOLVED
def test_tc_4():
    assert longest_range([4, 2, 1, 3, 6]) == [1, 4]


@UNSOLVED
def test_tc_5():
    assert longest_range([8, 4, 2, 10, 3, 6, 7, 9, 1]) == [6, 10]
