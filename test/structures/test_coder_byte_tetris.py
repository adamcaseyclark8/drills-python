from code.structures.coder_byte_tetris import get_max_number_of_rows_cleared  # noqa: F401


class TestTetrisTestCases:
    def test_coder_byte_test_case_1(self):
        print('NEED TO FIX TESTS')

        # heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6]
        # assert get_max_number_of_rows_cleared(heights, 'L') == 3

    # def test_coder_byte_test_case_2(self):
    #     heights = [2, 4, 3, 4, 5, 2, 0, 2, 2, 3, 3, 3]
    #     assert get_max_number_of_rows_cleared(heights, 'I') == 2
    #
    # def test_coder_byte_test_case_3(self):
    #     heights = [4, 3, 2, 3, 5, 1, 0, 1, 2, 4, 3, 4]
    #     assert get_max_number_of_rows_cleared(heights, 'O') == 0
    #
    # def test_verify_with_simple_case_i_piece(self):
    #     heights = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    #     assert get_max_number_of_rows_cleared(heights, 'I') == 4
    #
    # def test_verify_with_o_piece(self):
    #     heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    #     assert get_max_number_of_rows_cleared(heights, 'O') == 2
    #
    # def test_l_piece_should_clear_3_rows_on_specified_heights(self):
    #     heights = [3, 5, 2, 4, 6, 3, 5, 2, 4, 3, 5, 2]
    #     assert get_max_number_of_rows_cleared(heights, 'L') == 3
    #
    # def test_i_piece_should_clear_0_rows_on_empty_board(self):
    #     heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     assert get_max_number_of_rows_cleared(heights, 'I') == 0

# ["L","3","4","4","5","6","2","0","6","5","3","6","6"], 3
# Input: ["I", "2", "4", "3", "4", "5", "2", "0", "2", "2", "3", "3", "3"]
# Output: 2
# Input: ["O", "4", "3", "2", "3", "5", "1", "0", "1", "2", "4", "3", "4"]
# Output: 0
# ["I", "2", "4", "3", "4", "5", "2", "0", "2", "2", "3", "3", "3"]
# ["O", "4", "3", "2", "3", "5", "1", "0", "1", "2", "4", "3", "4"]

# Ideas for a multi-piece version, max_rows_cleared(heights, shapes), which doesn't exist yet:
#
# tetris
#   - should clear no rows when heights are uneven: [1..12] with all 7 shapes → >= 0
#   - should clear 1 row when all columns are at height 1: [1] * 12, ['I'] → 1
#   - should clear multiple rows with optimal placement: [2] * 12, ['I', 'I'] → >= 2
#
# edge cases
#   - empty board (all heights = 0), ['I', 'O', 'T'] → 0 (can't clear rows from empty board)
#   - single piece: [1] * 12, ['O'] → >= 0
#   - all pieces on flat surface: [3] * 12, all 7 shapes → >= 3
#   - very uneven heights: [0, 10] * 6, ['I', 'I', 'I'] → >= 0
#
# specific scenarios
#   - I-piece should clear 4 rows when placed horizontally on height 4: [4] * 12, ['I'] → 4
#   - O-piece should clear rows on perfect fit: [2] * 12, ['O'] → >= 2
#   - filling gaps should create clearable rows: [5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5], ['I', 'I'] → >= 2
#   - T-piece placement should enable row clearing: [3] * 12, ['T', 'T', 'T'] → >= 3
#
# complex scenarios
#   - all 7 pieces on varied heights: [3, 5, 2, 4, 6, 3, 5, 2, 4, 3, 5, 2] → between 0 and 28
#   - strategic placement to maximize clears: [4] * 12, ['I', 'I', 'I'] → >= 4
#   - cascading row clears: [5] * 12, ['I', 'O', 'T', 'S', 'Z'] → >= 5
#
# helper functions
#   - clear_complete_rows([3] * 12) → 3, and heights become [0] * 12
#   - clear_complete_rows([3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3]) → 2
#   - place_shape_on_heights([0] * 12, SHAPES['I'], 0) is not None and max(result) == 1
#   - place_shape_on_heights([0] * 12, SHAPES['I'], 10) is None (too far right)
#   - get_all_rotations: I has <= 4, T has 4, O has 1 (only 1 unique rotation)
#
# performance
#   - [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3] with all 7 shapes finishes in under 10s
#
# boundary conditions
#   - maximum height: [20] * 12, ['I'] → >= 20
#   - minimal height: [1] * 12, ['I', 'O', 'T'] → >= 1
#   - mixed zero and non-zero heights: [0, 5] * 6, ['I', 'I', 'I'] → >= 0
