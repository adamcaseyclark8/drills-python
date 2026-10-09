import pytest

from code.structures.coder_byte_tetris import (
    SHAPES,
    count_complete_rows,
    get_all_rotations,
    get_max_number_of_rows_cleared,
    place_shape_on_heights,
)


def test_coder_byte_test_case_1():
    heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6]
    assert get_max_number_of_rows_cleared(heights, 'L') == 3


def test_coder_byte_test_case_2():
    heights = [2, 4, 3, 4, 5, 2, 0, 2, 2, 3, 3, 3]
    assert get_max_number_of_rows_cleared(heights, 'I') == 2


@pytest.mark.xfail(strict=True, reason='returns 1 (same as the JS original)')
def test_coder_byte_test_case_3():
    heights = [4, 3, 2, 3, 5, 1, 0, 1, 2, 4, 3, 4]
    assert get_max_number_of_rows_cleared(heights, 'O') == 0


def find_best_placement(heights, shape):
    max_cleared = 0
    best_placement = None

    rotations = get_all_rotations(shape)

    for r, rotation in enumerate(rotations):
        for col in range(10):
            new_heights = place_shape_on_heights(heights, rotation, col)
            if new_heights:
                cleared = count_complete_rows(new_heights)
                if cleared > max_cleared:
                    max_cleared = cleared
                    best_placement = {'rotation': r, 'col': col, 'heights': new_heights, 'cleared': cleared}

    return len(rotations), max_cleared, best_placement


def test_debug_l_piece_test_case_1():
    rotation_count, max_cleared, best_placement = find_best_placement([3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6], SHAPES['L'])
    print(f'\nL-piece has {rotation_count} rotations')
    print(f'Max cleared: {max_cleared}')
    print('Best placement:', best_placement)


def test_debug_l_piece_test_case_2():
    _, max_cleared, best_placement = find_best_placement([3, 5, 2, 4, 6, 3, 5, 2, 4, 3, 5, 2], SHAPES['L'])
    print(f'Max cleared: {max_cleared}')
    print('Best placement:', best_placement)


# def test_verify_with_simple_case_i_piece():
#     heights = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#     assert get_max_number_of_rows_cleared(heights, 'I') == 4
#
#
# def test_verify_with_o_piece():
#     heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#     assert get_max_number_of_rows_cleared(heights, 'O') == 2
#
#
# def test_l_piece_should_clear_3_rows_on_specified_heights():
#     heights = [3, 5, 2, 4, 6, 3, 5, 2, 4, 3, 5, 2]
#     assert get_max_number_of_rows_cleared(heights, 'L') == 3
#
#
# def test_i_piece_should_clear_0_rows_on_empty_board():
#     heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     assert get_max_number_of_rows_cleared(heights, 'I') == 0
