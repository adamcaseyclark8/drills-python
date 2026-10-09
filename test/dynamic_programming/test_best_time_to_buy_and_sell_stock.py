from code.dynamic_programming.best_time_to_buy_and_sell_stock import best_time_to_buy_and_sell_stock


def test_returns_max_profit_for_standard_case():
    assert best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]) == 5


def test_returns_0_when_prices_only_decrease():
    assert best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]) == 0


def test_returns_profit_when_best_buy_is_first_element():
    assert best_time_to_buy_and_sell_stock([1, 2, 3, 4, 5]) == 4


def test_returns_profit_for_two_element_array():
    assert best_time_to_buy_and_sell_stock([1, 5]) == 4


def test_returns_0_for_two_equal_prices():
    assert best_time_to_buy_and_sell_stock([3, 3]) == 0


def test_returns_0_for_single_element():
    assert best_time_to_buy_and_sell_stock([5]) == 0


def test_returns_0_for_empty_array():
    assert best_time_to_buy_and_sell_stock([]) == 0


def test_handles_valley_before_peak_mid_array():
    assert best_time_to_buy_and_sell_stock([3, 10, 1, 9]) == 8
