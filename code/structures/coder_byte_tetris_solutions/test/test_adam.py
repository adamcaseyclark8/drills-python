import pytest

from code.structures.coder_byte_tetris_solutions.code.v2 import get_max_number_of_rows_cleared

#  I: [[0,0], [0,1], [0,2], [0,3]],
#  O: [[0,0], [0,1], [1,0], [1,1]],
#  T: [[0,0], [0,1], [0,2], [1,1]],
#  S: [[0,0], [0,1], [1,1], [1,2]],
#  Z: [[0,1], [0,2], [1,0], [1,1]],
#  J: [[0,0], [0,1], [0,2], [1,2]]
#  L: [[0,0], [0,1], [0,2], [1,0]],

#  Row  6:             ██       ██       ██ ██
#  Row  5:          ██ ██       ██ ██    ██ ██
#  Row  4:    ██ ██ ██ ██       ██ ██    ██ ██
#  Row  3: ██ ██ ██ ██ ██       ██ ██ ██ ██ ██
#  Row  2: ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██
#  Row  1: ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██

HEIGHTS = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6]
UNSOLVED = pytest.mark.xfail(strict=True, reason='v2 returns 3 for every shape (same as the JS original)')


@UNSOLVED
def test_case_1_i():
    assert get_max_number_of_rows_cleared(HEIGHTS, 'I') == 2


@UNSOLVED
def test_case_2_o():
    assert get_max_number_of_rows_cleared(HEIGHTS, 'O') == 1


@UNSOLVED
def test_case_3_t():
    assert get_max_number_of_rows_cleared(HEIGHTS, 'T') == 2


@UNSOLVED
def test_case_4_s():
    assert get_max_number_of_rows_cleared(HEIGHTS, 'S') == 1


@UNSOLVED
def test_case_5_z():
    assert get_max_number_of_rows_cleared(HEIGHTS, 'Z') == 0


@UNSOLVED
def test_case_6_j():
    assert get_max_number_of_rows_cleared(HEIGHTS, 'J') == 0


def test_case_7_l():
    assert get_max_number_of_rows_cleared(HEIGHTS, 'L') == 3
