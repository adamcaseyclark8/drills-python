import importlib

# `02_product_sum` isn't a valid identifier, so it can't appear in an import statement
product_sum = importlib.import_module('misc.algo_experts.recursion.02_product_sum.code.index').product_sum


def test_sample_input_gets_sample_output():
    assert product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12


def test_case_1():
    assert product_sum([1, 2, 3, 4, 5]) == 15


def test_case_2():
    assert product_sum([1, 2, [3], 4, 5]) == 18


def test_case_3():
    assert product_sum([[1, 2], 3, [4, 5]]) == 27
