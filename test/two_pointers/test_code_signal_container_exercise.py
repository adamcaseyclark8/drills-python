from code.two_pointers.code_signal_container_exercise import code_signal_container_exercise

ADD = 'ADD'
EXISTS = 'EXISTS'
REMOVE = 'REMOVE'
NEXT_UP = 'NEXT_UP'


def test_i_add():
    queries = [[ADD, '1'], [ADD, '2'], [ADD, '3'], [ADD, '4'], [ADD, '5']]
    assert code_signal_container_exercise(queries) == ['', '', '', '', '']


def test_ii_exists():
    queries = [[ADD, '1'], [ADD, '2'], [EXISTS, '1'], [EXISTS, '2'], [EXISTS, '3']]
    assert code_signal_container_exercise(queries) == ['', '', 'true', 'true', 'false']


def test_iii_remove():
    queries = [
        [ADD, '1'],
        [ADD, '2'],
        [ADD, '3'],
        [ADD, '4'],
        [REMOVE, '2'],
        [EXISTS, '2'],
        [REMOVE, '4'],
        [EXISTS, '4'],
        [EXISTS, '3'],
    ]
    assert code_signal_container_exercise(queries) == ['', '', '', '', 'true', 'false', 'true', 'false', 'true']


def test_iv_next_up():
    queries = [
        [ADD, '1'],
        [ADD, '5'],
        [ADD, '6'],
        [ADD, '9'],
        [NEXT_UP, '1'],
        [NEXT_UP, '5'],
        [NEXT_UP, '6'],
        [NEXT_UP, '9'],
    ]
    assert code_signal_container_exercise(queries) == ['', '', '', '', '5', '6', '9', '']
