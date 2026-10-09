import pytest

from code.linked_lists.singly_linked_list import List


@pytest.fixture
def linked_list():
    return List()


def test_push_adds_nodes_to_the_end(linked_list):
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.to_array() == [1, 2, 3]
    assert linked_list.length == 3


def test_pop_removes_the_last_node(linked_list):
    linked_list.push(1)
    linked_list.push(2)
    popped = linked_list.pop()
    assert popped.value == 2
    assert linked_list.to_array() == [1]
    assert linked_list.length == 1

    popped2 = linked_list.pop()
    assert popped2.value == 1
    assert linked_list.to_array() == []
    assert linked_list.length == 0

    assert linked_list.pop() is None


def test_delete_removes_the_first_occurrence_of_value(linked_list):
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(2)

    deleted = linked_list.delete(2)
    assert deleted.value == 2
    assert linked_list.to_array() == [1, 3, 2]
    assert linked_list.length == 3

    deleted2 = linked_list.delete(2)
    assert deleted2.value == 2
    assert linked_list.to_array() == [1, 3]
    assert linked_list.length == 2

    assert linked_list.delete(4) is None


def test_find_returns_the_node_with_given_value(linked_list):
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)

    assert linked_list.find(2).value == 2
    assert linked_list.find(4) is None


def test_handles_operations_on_empty_list(linked_list):
    assert linked_list.pop() is None
    assert linked_list.delete(1) is None
    assert linked_list.find(1) is None
    assert linked_list.to_array() == []
