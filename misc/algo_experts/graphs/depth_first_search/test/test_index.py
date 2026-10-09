from ..code.index import Node


def test_case_1():
    test1 = Node('A')
    test1.add_child('B').add_child('C')
    test1.children[0].add_child('D')

    assert test1.depth_first_search([]) == ['A', 'B', 'D', 'C']


def test_case_2():
    test2 = Node('A')
    test2.add_child('B').add_child('C').add_child('D').add_child('E')
    test2.children[1].add_child('F')

    assert test2.depth_first_search([]) == ['A', 'B', 'C', 'F', 'D', 'E']


def test_case_3():
    pass
