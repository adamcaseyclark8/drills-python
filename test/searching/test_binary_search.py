from code.searching.binary_search import perform_binary_search


def test_case_1():
    assert perform_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33) == 3


def test_case_2():
    assert perform_binary_search([1, 5, 23, 111], 5) == 1


def test_case_3():
    assert perform_binary_search([1, 5, 23, 111], 35) == -1


def test_case_4():
    assert perform_binary_search([1, 5, 23, 111], 111) == 3


def test_case_5():
    assert perform_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 72) == 8


def test_case_6():
    assert perform_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73) == 9


def test_case_7():
    assert perform_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 70) == -1


def test_case_8():
    assert perform_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355) == 10


def test_case_9():
    assert perform_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 354], 355) == -1
