from code.sliding_window.buy_sell_stock import best_time_to_buy_or_sell_stock


def test_misc_scenario():
    assert best_time_to_buy_or_sell_stock([7, 1, 5, 3, 6, 4]) == 5  # Buy at 1, sell at 6


def test_decreasing_prices():
    assert best_time_to_buy_or_sell_stock([7, 6, 4, 3, 1]) == 0  # No profit possible


def test_empty_array():
    assert best_time_to_buy_or_sell_stock([]) == 0


def test_single_day_price():
    assert best_time_to_buy_or_sell_stock([5]) == 0  # Cannot sell


def test_prices_remain_constant():
    assert best_time_to_buy_or_sell_stock([3, 3, 3, 3, 3]) == 0


def test_large_profit_late_in_array():
    assert best_time_to_buy_or_sell_stock([10, 2, 1, 5, 6, 20]) == 19  # Buy at 1, sell at 20


def test_profit_happens_after_multiple_drops():
    assert best_time_to_buy_or_sell_stock([9, 7, 4, 1, 5, 8]) == 7  # Buy at 1, sell at 8


def test_two_elements_increasing():
    assert best_time_to_buy_or_sell_stock([2, 4]) == 2


def test_two_elements_decreasing():
    assert best_time_to_buy_or_sell_stock([5, 3]) == 0


def test_multiple_peaks_and_valleys():
    assert best_time_to_buy_or_sell_stock([3, 2, 6, 1, 4]) == 4  # Buy at 2, sell at 6
