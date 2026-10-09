import importlib

# `01_kadanes` isn't a valid identifier, so it can't appear in an import statement
kadanes = importlib.import_module('misc.algo_experts.famous_algorithms.01_kadanes.code.index_by_algo').kadanes


def test_case_1():
    assert kadanes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55


def test_case_2():
    assert kadanes([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1


def test_case_3():
    assert kadanes([-10, -2, -9, -4, -8, -6, -7, -1, -5]) == -1


def test_case_4():
    assert kadanes([1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]) == 35


# expected results for test cases 5 - 13 (inputs not written yet):
# 34, 11, 16, 19, 23, 24, 22, 35, 135
