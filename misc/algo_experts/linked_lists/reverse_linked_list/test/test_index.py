from ..code.index import reverse_linked_list


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_many(self, values):
        current = self

        while current.next is not None:
            current = current.next

        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def get_nodes_in_array(self):
        nodes = []
        current = self

        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def test_case_1():
    result = reverse_linked_list(LinkedList(0)).get_nodes_in_array()
    expected = LinkedList(0).get_nodes_in_array()
    assert result == expected


def test_case_2():
    result = reverse_linked_list(LinkedList(0).add_many([1])).get_nodes_in_array()
    expected = LinkedList(1).add_many([0]).get_nodes_in_array()
    assert result == expected
