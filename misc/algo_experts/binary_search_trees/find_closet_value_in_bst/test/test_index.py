import pytest

from ..code.index import find_closest_value_in_bst  # noqa: F401


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    def __repr__(self):
        return f'BST(value={self.value}, left={self.left}, right={self.right})'


@pytest.fixture
def tree():
    tree = BST(100)
    for value in [5, 15, 5, 2, 1, 22, 1, 1, 3, 1, 1, 502, 55000, 204, 205, 207, 206, 208, 203, -51, -403, 1001, 57,
                  60, 4500]:
        tree.insert(value)
    return tree


def test_case_1(tree):
    print(tree)


# def test_case_1(tree):
#     assert find_closest_value_in_bst(tree, 100) == 100
#
#
# def test_case_2(tree):
#     assert find_closest_value_in_bst(tree, 208) == 208
#
#
# def test_case_3(tree):
#     assert find_closest_value_in_bst(tree, 4500) == 4500
#
#
# def test_case_4(tree):
#     assert find_closest_value_in_bst(tree, 4501) == 4500
