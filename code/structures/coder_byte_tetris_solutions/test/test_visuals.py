from code.structures.coder_byte_tetris import (
    SHAPES,
    count_complete_rows,
    get_all_rotations,
    place_shape_on_heights,
)


# Add this helper function to your test file
def visualize_board(heights, title=''):
    max_height = max(heights)
    print(f'\n{title}')
    print('Column: ', ' '.join(str(i).rjust(2) for i in range(len(heights))))
    print('Height: ', ' '.join(str(h).rjust(2) for h in heights))
    print('')

    # Draw the board from top to bottom
    for row in range(max_height, 0, -1):
        line = ' '.join('██' if h >= row else '  ' for h in heights)
        print(f'Row {str(row).rjust(2)}: {line}')
    print('       ' + '══ ' * len(heights))

    # Check which rows are complete
    print('\nComplete rows:')
    for level in range(1, max_height + 1):
        if all(h >= level for h in heights):
            print(f'  Row {level}: COMPLETE ✓')


def test_visualize_test_case_1_l_piece():
    heights = [3, 4, 4, 5, 6, 2, 0, 6, 5, 3, 6, 6]
    visualize_board(heights, 'Test Case #1: Initial State')

    # Best placement from debug
    after_l = [3, 4, 4, 5, 7, 7, 8, 6, 5, 3, 6, 6]
    visualize_board(after_l, 'After L-piece at col 4, rotation 0')


def test_visualize_test_case_2_i_piece():
    heights = [2, 4, 3, 4, 5, 2, 0, 2, 2, 3, 3, 3]
    visualize_board(heights, 'Test Case #2: Initial State')

    # Try to find best I placement
    rotations = get_all_rotations(SHAPES['I'])
    best_result = None
    max_cleared = 0

    for r, rotation in enumerate(rotations):
        for col in range(12):
            new_heights = place_shape_on_heights(heights, rotation, col)
            if new_heights:
                cleared = count_complete_rows(new_heights)
                if cleared > max_cleared:
                    max_cleared = cleared
                    best_result = {'new_heights': new_heights, 'col': col, 'rotation': r}

    if best_result:
        visualize_board(
            best_result['new_heights'],
            f"After I-piece at col {best_result['col']}, rotation {best_result['rotation']} ({max_cleared} rows cleared)",
        )


def test_visualize_test_case_3_o_piece():
    heights = [4, 3, 2, 3, 5, 1, 0, 1, 2, 4, 3, 4]
    visualize_board(heights, 'Test Case #3: Initial State')

    # Show best O placement
    after_o_col5 = [4, 3, 2, 3, 5, 3, 3, 1, 2, 4, 3, 4]
    visualize_board(after_o_col5, 'After O-piece at col 5 (my algorithm says 1 row, test expects 0)')

    # Show another placement
    after_o_col6 = [4, 3, 2, 3, 5, 1, 3, 3, 2, 4, 3, 4]
    visualize_board(after_o_col6, 'After O-piece at col 6 (my algorithm says 1 row, test expects 0)')


def test_visualize_l_piece_on_varied_heights():
    heights = [3, 5, 2, 4, 6, 3, 5, 2, 4, 3, 5, 2]
    visualize_board(heights, 'L-piece test: Initial State (expects 3 rows cleared)')

    # My best result
    my_best = [6, 6, 7, 4, 6, 3, 5, 2, 4, 3, 5, 2]
    visualize_board(my_best, 'After L-piece at col 0, rotation 0 (I get 2 rows, expects 3)')
