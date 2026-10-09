from code.dynamic_programming.find_number_of_coin_combinations import find_number_of_coin_combinations


def test_example_case_amount_5_coins_1_2_5():
    assert find_number_of_coin_combinations(5, [1, 2, 5]) == 4


def test_no_combinations_possible():
    assert find_number_of_coin_combinations(3, [2]) == 0


def test_amount_is_zero_one_way_use_nothing():
    assert find_number_of_coin_combinations(0, [1, 2, 5]) == 1


def test_single_coin_that_divides_evenly():
    assert find_number_of_coin_combinations(6, [3]) == 1


def test_single_coin_that_does_not_divide_evenly():
    assert find_number_of_coin_combinations(7, [3]) == 0


def test_all_ones_only_one_combination():
    assert find_number_of_coin_combinations(4, [1]) == 1


def test_larger_amount():
    assert find_number_of_coin_combinations(10, [1, 2, 5]) == 10


def test_order_does_not_matter_combinations_not_permutations():
    assert find_number_of_coin_combinations(4, [1, 2]) == 3
