import pytest

from ..code.index import DoublyLinkedList, Node


def expect_empty(linked_list):
    assert linked_list.head is None
    assert linked_list.tail is None


def expect_head_tail(linked_list, head, tail):
    assert linked_list.head is head
    assert linked_list.tail is tail


def expect_single_node(linked_list, node):
    assert linked_list.head is node
    assert linked_list.tail is node


def get_node_values_head_to_tail(linked_list):
    values = []
    node = linked_list.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def get_node_values_tail_to_head(linked_list):
    values = []
    node = linked_list.tail
    while node is not None:
        values.append(node.value)
        node = node.previous
    return values


def remove_nodes(linked_list, nodes):
    for node in nodes:
        linked_list.remove(node)


@pytest.fixture
def linked_list():
    return DoublyLinkedList()


@pytest.fixture
def nodes():
    return [Node(value) for value in range(1, 8)]


def test_case_1(linked_list, nodes):
    first = nodes[0]
    node = None  # never assigned in the original test

    linked_list.set_head(first)
    expect_single_node(linked_list, first)
    linked_list.remove(first)
    expect_empty(linked_list)
    linked_list.set_tail(first)
    expect_single_node(linked_list, first)
    linked_list.remove_nodes_with_value(1)
    expect_empty(linked_list)
    linked_list.insert_at_position(1, node)
    expect_single_node(linked_list, node)


def test_case_2(linked_list, nodes):
    first, second = nodes[:2]
    pair = [first, second]

    linked_list.set_head(first)
    linked_list.set_tail(second)
    expect_head_tail(linked_list, first, second)
    remove_nodes(linked_list, pair)
    expect_empty(linked_list)

    linked_list.set_head(first)
    linked_list.insert_after(first, second)
    expect_head_tail(linked_list, first, second)
    remove_nodes(linked_list, pair)
    expect_empty(linked_list)

    linked_list.set_head(first)
    linked_list.insert_before(first, second)
    expect_head_tail(linked_list, second, first)
    remove_nodes(linked_list, pair)
    expect_empty(linked_list)

    linked_list.insert_at_position(1, first)
    linked_list.insert_at_position(2, second)
    expect_head_tail(linked_list, first, second)
    remove_nodes(linked_list, pair)
    expect_empty(linked_list)

    # linked_list.insert_at_position(2, first)
    # linked_list.insert_at_position(1, second)
    # expect_head_tail(linked_list, second, first)


def test_case_3(linked_list, nodes):
    first, second, third, fourth = nodes[:4]

    linked_list.set_head(first)
    assert linked_list.contains_node_with_value(1) is True
    linked_list.insert_after(first, second)
    assert linked_list.contains_node_with_value(2) is True
    linked_list.insert_after(second, third)
    assert linked_list.contains_node_with_value(3) is True
    linked_list.insert_after(third, fourth)
    assert linked_list.contains_node_with_value(4) is True
    linked_list.remove_nodes_with_value(3)
    assert linked_list.contains_node_with_value(3) is False
    linked_list.remove(first)
    assert linked_list.contains_node_with_value(1) is False
    linked_list.remove_nodes_with_value(4)
    assert linked_list.contains_node_with_value(4) is False
    linked_list.remove(second)
    assert linked_list.contains_node_with_value(2) is False


def test_case_4(linked_list, nodes):
    first, second, third, fourth, fifth, sixth, seventh = nodes

    linked_list.set_head(first)
    linked_list.insert_after(first, second)
    linked_list.insert_after(second, third)
    linked_list.insert_after(third, fourth)
    linked_list.insert_after(fourth, fifth)
    linked_list.insert_after(fifth, sixth)
    linked_list.insert_after(sixth, seventh)

    assert get_node_values_head_to_tail(linked_list) == [1, 2, 3, 4, 5, 6, 7]
    assert get_node_values_tail_to_head(linked_list) == [7, 6, 5, 4, 3, 2, 1]
    expect_head_tail(linked_list, first, seventh)
    linked_list.remove(second)
    assert get_node_values_head_to_tail(linked_list) == [1, 3, 4, 5, 6, 7]
    assert get_node_values_tail_to_head(linked_list) == [7, 6, 5, 4, 3, 1]
    expect_head_tail(linked_list, first, seventh)
    linked_list.remove_nodes_with_value(1)
    assert get_node_values_head_to_tail(linked_list) == [3, 4, 5, 6, 7]
    assert get_node_values_tail_to_head(linked_list) == [7, 6, 5, 4, 3]
    expect_head_tail(linked_list, third, seventh)
    linked_list.remove_nodes_with_value(3)
    assert get_node_values_head_to_tail(linked_list) == [4, 5, 6, 7]
    assert get_node_values_tail_to_head(linked_list) == [7, 6, 5, 4]
    expect_head_tail(linked_list, fourth, seventh)
    linked_list.remove_nodes_with_value(4)
    linked_list.remove_nodes_with_value(5)
    linked_list.remove_nodes_with_value(7)
    assert get_node_values_head_to_tail(linked_list) == [6]
    assert get_node_values_tail_to_head(linked_list) == [6]
    expect_head_tail(linked_list, sixth, sixth)


def test_case_5(linked_list, nodes):
    first, second, third, fourth, fifth = nodes[:5]

    linked_list.set_head(first)
    linked_list.insert_after(first, second)
    linked_list.insert_after(second, third)
    linked_list.insert_after(third, fourth)

    linked_list.insert_after(fourth, fifth)
    assert get_node_values_head_to_tail(linked_list) == [1, 2, 3, 4, 5]
    expect_head_tail(linked_list, first, fifth)

    linked_list.insert_after(third, fifth)
    assert get_node_values_head_to_tail(linked_list) == [1, 2, 3, 5, 4]
    expect_head_tail(linked_list, first, fourth)

    linked_list.insert_after(third, first)
    assert get_node_values_head_to_tail(linked_list) == [2, 3, 1, 5, 4]
    expect_head_tail(linked_list, second, fourth)

    # linked_list.insert_after(fifth, second)
    # assert get_node_values_head_to_tail(linked_list) == [3, 1, 5, 2, 4]
    # expect_head_tail(linked_list, third, fourth)
    #
    # linked_list.insert_after(fourth, sixth)
    # assert get_node_values_head_to_tail(linked_list) == [3, 1, 5, 2, 4, 6]
    # expect_head_tail(linked_list, third, sixth)
    #
    # linked_list.insert_after(second, seventh)
    # assert get_node_values_head_to_tail(linked_list) == [3, 1, 5, 2, 7, 4, 6]
    # expect_head_tail(linked_list, third, sixth)


def test_case_6(linked_list, nodes):
    first, second, third, fourth, fifth = nodes[:5]

    linked_list.set_head(first)
    linked_list.insert_before(first, second)
    linked_list.insert_before(second, third)
    linked_list.insert_before(third, fourth)

    linked_list.insert_before(fourth, fifth)
    assert get_node_values_head_to_tail(linked_list) == [5, 4, 3, 2, 1]
    expect_head_tail(linked_list, fifth, first)

    linked_list.insert_before(third, first)
    assert get_node_values_head_to_tail(linked_list) == [5, 4, 1, 3, 2]
    expect_head_tail(linked_list, fifth, second)

    linked_list.insert_before(fifth, second)
    assert get_node_values_head_to_tail(linked_list) == [2, 5, 4, 1, 3]
    expect_head_tail(linked_list, second, third)

    # linked_list.insert_before(fifth, fourth)
    # assert get_node_values_head_to_tail(linked_list) == [2, 4, 5, 1, 3]
    # expect_head_tail(linked_list, second, third)
    #
    # linked_list.insert_before(second, sixth)
    # assert get_node_values_head_to_tail(linked_list) == [6, 2, 4, 5, 1, 3]
    # expect_head_tail(linked_list, sixth, third)
    #
    # linked_list.insert_before(first, seventh)
    # assert get_node_values_head_to_tail(linked_list) == [6, 2, 4, 5, 7, 1, 3]
    # expect_head_tail(linked_list, sixth, third)


def test_case_7(linked_list, nodes):
    first, second, third, fourth, fifth, sixth, seventh = nodes

    linked_list.set_head(first)
    linked_list.insert_at_position(1, second)
    linked_list.insert_at_position(1, third)
    linked_list.insert_at_position(1, fourth)
    linked_list.insert_at_position(1, fifth)

    assert get_node_values_head_to_tail(linked_list) == [5, 4, 3, 2, 1]
    expect_head_tail(linked_list, fifth, first)

    linked_list.insert_at_position(2, first)
    assert get_node_values_head_to_tail(linked_list) == [5, 1, 4, 3, 2]
    expect_head_tail(linked_list, fifth, second)

    linked_list.insert_at_position(1, second)
    assert get_node_values_head_to_tail(linked_list) == [2, 5, 1, 4, 3]
    expect_head_tail(linked_list, second, third)

    linked_list.insert_at_position(2, fourth)
    assert get_node_values_head_to_tail(linked_list) == [2, 4, 5, 1, 3]
    expect_head_tail(linked_list, second, third)

    linked_list.insert_at_position(1, sixth)
    assert get_node_values_head_to_tail(linked_list) == [6, 2, 4, 5, 1, 3]
    expect_head_tail(linked_list, sixth, third)

    linked_list.insert_at_position(5, seventh)
    assert get_node_values_head_to_tail(linked_list) == [6, 2, 4, 5, 7, 1, 3]
    expect_head_tail(linked_list, sixth, third)

    linked_list.insert_at_position(8, fourth)
    assert get_node_values_head_to_tail(linked_list) == [6, 2, 5, 7, 1, 3, 4]
    expect_head_tail(linked_list, sixth, fourth)
