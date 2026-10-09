from code.dynamic_programming.get_least_number_of_coins import get_least_number_of_coins


def test_1_5_10_25_amount_36_returns_3():
    assert get_least_number_of_coins([1, 5, 10, 25], 36) == 3


def test_1_2_5_amount_11_returns_3():
    assert get_least_number_of_coins([1, 2, 5], 11) == 3


def test_2_amount_3_returns_minus_1():
    assert get_least_number_of_coins([2], 3) == -1


def test_1_amount_0_returns_0():
    assert get_least_number_of_coins([1], 0) == 0


def test_1_amount_1_returns_1():
    assert get_least_number_of_coins([1], 1) == 1


def test_1_amount_5_returns_5():
    assert get_least_number_of_coins([1], 5) == 5


def test_exact_match_returns_1():
    assert get_least_number_of_coins([5, 10, 25], 25) == 1


def test_no_solution_returns_minus_1():
    assert get_least_number_of_coins([5, 10], 3) == -1
