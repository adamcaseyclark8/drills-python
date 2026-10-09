from code.math.expected_goals_scored import expected_goals_range


def test_returns_a_single_value_range_for_constant_inputs():
    assert expected_goals_range([2, 2, 2], [2, 2, 2], [10, 10, 10], [10, 10, 10]) == {'low': 2, 'high': 2}


def test_returns_zero_range_when_all_inputs_are_zero_without_nan():
    assert expected_goals_range([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) == {'low': 0, 'high': 0}


def test_returns_integers_with_low_less_than_or_equal_to_high():
    results = expected_goals_range([1, 3, 0, 2], [2, 1, 4, 1], [12, 15, 8, 11], [9, 14, 13, 10])
    assert isinstance(results['low'], int)
    assert isinstance(results['high'], int)
    assert results['low'] <= results['high']


def test_never_returns_a_negative_low_value():
    results = expected_goals_range([0, 6, 0, 6], [0, 6, 0, 6], [10, 10, 10, 10], [10, 10, 10, 10])
    assert results['low'] >= 0


def test_weights_recent_games_more_heavily():
    recent_high = expected_goals_range([0, 0, 0, 4], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10])
    recent_low = expected_goals_range([4, 0, 0, 0], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10])
    assert recent_high['high'] > recent_low['high']


def test_treats_all_games_equally_when_decay_is_1():
    recent_high = expected_goals_range([0, 0, 0, 4], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10], 1)
    recent_low = expected_goals_range([4, 0, 0, 0], [1, 1, 1, 1], [10, 10, 10, 10], [10, 10, 10, 10], 1)
    assert recent_high == recent_low


def test_ignores_attempts_when_attempts_weight_is_0():
    few_attempts = expected_goals_range([1, 2, 3], [2, 2, 2], [5, 5, 5], [5, 5, 5], 0.8, 0)
    many_attempts = expected_goals_range([1, 2, 3], [2, 2, 2], [30, 30, 30], [30, 30, 30], 0.8, 0)
    assert few_attempts == many_attempts


def test_raises_the_estimate_when_the_opponent_gives_up_more_attempts():
    results = expected_goals_range([2, 2, 2], [2, 2, 2], [10, 10, 10], [30, 30, 30], 0.8, 1)
    assert results == {'low': 2, 'high': 3}
