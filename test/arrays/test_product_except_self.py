from code.arrays.product_except_self import product_except_self


def test_basic_case():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_contains_zero():
    assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]


def test_two_elements():
    assert product_except_self([3, 4]) == [4, 3]


def test_all_ones():
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]


def test_single_element():
    assert product_except_self([5]) == [1]


def test_contains_negative_numbers():
    assert product_except_self([-1, 2, 3]) == [6, -3, -2]
