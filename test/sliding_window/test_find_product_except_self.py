from code.sliding_window.find_product_except_self import find_product_except_self


def test_1_2_3_4_returns_24_12_8_6():
    assert find_product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_two_elements_returns_reversed_values():
    assert find_product_except_self([3, 4]) == [4, 3]


def test_array_with_a_zero():
    assert find_product_except_self([1, 0, 3]) == [0, 3, 0]


def test_array_with_two_zeros_returns_all_zeros():
    assert find_product_except_self([0, 0, 3]) == [0, 0, 0]


def test_all_ones_returns_all_ones():
    assert find_product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]


def test_negative_numbers():
    assert find_product_except_self([-2, -3, -4]) == [12, 8, 6]
