import importlib

# `02_find_three_largest` isn't a valid identifier, so it can't appear in an import statement
find_three_largest_numbers = importlib.import_module(
    'misc.algo_experts.searching.02_find_three_largest.code.index_by_algo'
).find_three_largest_numbers


def test_case_1():
    assert find_three_largest_numbers([55, 7, 8]) == [7, 8, 55]


def test_case_2():
    assert find_three_largest_numbers([55, 43, 11, 3, -3, 10]) == [11, 43, 55]


def test_case_3():
    assert find_three_largest_numbers([7, 8, 3, 11, 43, 55]) == [11, 43, 55]


def test_case_4():
    assert find_three_largest_numbers([55, 7, 8, 3, 43, 11]) == [11, 43, 55]


def test_case_5():
    assert find_three_largest_numbers([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7]


def test_case_6():
    assert find_three_largest_numbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]) == [7, 7, 8]


def test_case_7():
    assert find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541]


def test_case_8():
    assert find_three_largest_numbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]) == [-2, -1, 7]
