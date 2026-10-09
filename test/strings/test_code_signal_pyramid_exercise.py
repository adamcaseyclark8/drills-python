from code.strings.code_signal_pyramid_exercise import build_ascii_pyramid


def printed_rows(capsys):
    return capsys.readouterr().out.splitlines()


def test_creates_a_pyramid_with_n_1(capsys):
    build_ascii_pyramid(1)
    assert printed_rows(capsys) == ['*']


def test_creates_a_pyramid_with_n_3(capsys):
    build_ascii_pyramid(3)
    assert printed_rows(capsys) == ['  *', ' ***', '*****']


def test_creates_a_pyramid_with_n_5(capsys):
    build_ascii_pyramid(5)
    assert printed_rows(capsys) == ['    *', '   ***', '  *****', ' *******', '*********']


def test_creates_a_pyramid_with_n_10(capsys):
    build_ascii_pyramid(10)
    rows = printed_rows(capsys)
    assert len(rows) == 10
    assert rows[0] == '         *'
    assert rows[9] == '*******************'


def test_each_row_has_correct_number_of_leading_spaces_and_asterisks(capsys):
    n = 7
    build_ascii_pyramid(n)
    rows = printed_rows(capsys)

    for i in range(n):
        spaces = n - (i + 1)
        asterisks = 2 * (i + 1) - 1
        assert rows[i] == ' ' * spaces + '*' * asterisks


def test_each_row_has_correct_number_of_asterisks(capsys):
    n = 5
    build_ascii_pyramid(n)
    rows = printed_rows(capsys)

    for i in range(n):
        assert rows[i].count('*') == 2 * (i + 1) - 1


def test_first_row_has_only_one_asterisk(capsys):
    build_ascii_pyramid(4)
    assert printed_rows(capsys)[0].strip() == '*'


def test_last_row_has_no_leading_spaces(capsys):
    build_ascii_pyramid(6)
    assert printed_rows(capsys)[5][0] == '*'
