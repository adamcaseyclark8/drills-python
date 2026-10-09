from code.matrices.verify_tic_tac_toe import calculate_winner_in_tic_tac_toe


def test_returns_x_for_a_winning_row():
    squares = ['X', 'X', 'X', 'O', None, 'O', None, None, None]
    assert calculate_winner_in_tic_tac_toe(squares) == 'X'


def test_returns_o_for_a_winning_column():
    squares = ['O', 'X', None, 'O', 'X', None, 'O', None, 'X']
    assert calculate_winner_in_tic_tac_toe(squares) == 'O'


def test_returns_x_for_a_winning_diagonal_top_left_to_bottom_right():
    squares = ['X', 'O', None, None, 'X', 'O', None, None, 'X']
    assert calculate_winner_in_tic_tac_toe(squares) == 'X'


def test_returns_o_for_a_winning_diagonal_top_right_to_bottom_left():
    squares = ['X', None, 'O', None, 'O', 'X', 'O', None, None]
    assert calculate_winner_in_tic_tac_toe(squares) == 'O'


def test_returns_none_when_there_is_no_winner_yet():
    squares = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O']
    # board full, but no 3-in-a-row
    assert calculate_winner_in_tic_tac_toe(squares) is None


def test_returns_none_for_an_empty_board():
    assert calculate_winner_in_tic_tac_toe([None] * 9) is None


def test_returns_the_first_winning_line_found_top_priority():
    # Multiple lines possible, function stops at the first match
    squares = [
        'X', 'X', 'X',  # row 1 win
        'X', 'X', 'X',  # row 2 also win
        'O', 'O', 'O',
    ]
    # According to code order, first win found is top row
    assert calculate_winner_in_tic_tac_toe(squares) == 'X'
