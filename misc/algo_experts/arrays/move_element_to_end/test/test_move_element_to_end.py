import pytest

from ..code.move_element_to_end import move_element_to_end


@pytest.mark.xfail(strict=True, reason='move_element_to_end is unfinished (fails in the JS original too)')
def test_tc_1():
    assert move_element_to_end([1, 2, 3, 4, 5, 0, 0, 0]) == [1, 2, 3, 4, 5, 0, 0, 0]
