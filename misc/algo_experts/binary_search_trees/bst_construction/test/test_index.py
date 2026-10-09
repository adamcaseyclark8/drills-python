import pytest

from ..code.index import BST


@pytest.fixture
def test1():
    return BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)


def in_order_traverse(tree, array):
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


def test_case_1(test1):
    assert test1.left.value == 5


def test_case_2(test1):
    assert test1.right.right.value == 22


def test_case_3(test1):
    assert test1.right.left.value == 14


def test_case_4(test1):
    assert test1.left.right.value == 5


def test_case_5(test1):
    assert test1.left.left.value == 2


def test_case_6(test1):
    assert test1.left.left.left is None


def test_case_7(test1):
    assert test1.right.left.right is None


def test_case_8(test1):
    assert test1.contains(15) is True


def test_case_9(test1):
    assert test1.contains(2) is True


def test_case_10(test1):
    assert test1.contains(5) is True


def test_case_11(test1):
    assert test1.contains(10) is True


def test_case_12(test1):
    assert test1.contains(22) is True


def test_case_13(test1):
    assert test1.contains(23) is False


@pytest.mark.xfail(strict=True, reason='remove is unfinished (fails in the JS original too)')
def test_case_14():
    test2 = BST(10).insert(15).insert(11).insert(22).remove(10)
    assert in_order_traverse(test2, []) == [11, 15, 22]
