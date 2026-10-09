from code.linked_lists.detect_loop_in_a_linked_list import detect_loop_in_a_linked_list


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def test_when_linked_list_has_loop():
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = head.next

    # 1 => 3 => 4 => 3 (loop)

    assert detect_loop_in_a_linked_list(head) is True


def test_when_linked_list_has_no_loop():
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # 1 => 3 => 4 => 5

    assert detect_loop_in_a_linked_list(head) is False


def test_when_list_is_empty_none_head():
    assert detect_loop_in_a_linked_list(None) is False


def test_when_list_has_a_single_node_with_no_loop():
    assert detect_loop_in_a_linked_list(Node(1)) is False


def test_when_list_has_a_single_node_pointing_to_itself():
    head = Node(1)
    head.next = head

    assert detect_loop_in_a_linked_list(head) is True


def test_when_loop_is_at_the_tail_pointing_back_to_head():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = head

    # 1 => 2 => 3 => 1 (loop back to head)

    assert detect_loop_in_a_linked_list(head) is True


def test_when_list_has_two_nodes_with_no_loop():
    head = Node(1)
    head.next = Node(2)

    assert detect_loop_in_a_linked_list(head) is False


def test_when_list_has_two_nodes_with_a_loop():
    head = Node(1)
    head.next = Node(2)
    head.next.next = head

    # 1 => 2 => 1 (loop)

    assert detect_loop_in_a_linked_list(head) is True


def test_when_loop_connects_back_to_a_middle_node_in_a_longer_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next  # 5 => 3

    # 1 => 2 => 3 => 4 => 5 => 3 (loop)

    assert detect_loop_in_a_linked_list(head) is True
