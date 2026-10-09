from code.greedy.best_time_to_buy_sell_stock import best_time_to_buy_sell_stock


def test_returns_max_profit_for_typical_increasing_then_decreasing_prices():
    assert best_time_to_buy_sell_stock([7, 1, 5, 3, 6, 4]) == 5


def test_returns_0_when_prices_only_decrease():
    assert best_time_to_buy_sell_stock([7, 6, 4, 3, 1]) == 0


def test_returns_0_for_empty_array():
    assert best_time_to_buy_sell_stock([]) == 0


def test_returns_0_for_single_price():
    assert best_time_to_buy_sell_stock([5]) == 0


def test_returns_correct_profit_when_best_buy_sell_are_at_the_ends():
    assert best_time_to_buy_sell_stock([2, 4, 1, 7]) == 6


def test_handles_all_equal_prices():
    assert best_time_to_buy_sell_stock([3, 3, 3, 3]) == 0
