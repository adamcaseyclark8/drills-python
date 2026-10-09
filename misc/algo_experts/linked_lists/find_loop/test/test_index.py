from ..code.index import LinkedList, find_loop


class LinkedListImplementation(LinkedList):
    def add_many(self, values):
        current = self

        while current.next is not None:
            current = current.next

        for value in values:
            current.next = LinkedListImplementation(value)
            current = current.next
        return self

    def get_nth_node(self, n):
        counter = 1
        current = self

        while counter < n:
            current = current.next
            counter += 1
        return current


def test_case_1():
    test1 = LinkedListImplementation(0).add_many([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(LinkedListImplementation)

    test1.get_nth_node(10).next = test1.get_nth_node(1)
    assert find_loop(test1) is test1.get_nth_node(1)


def test_case_2():
    test2 = LinkedListImplementation(0).add_many([1, 2, 3, 4, 5, 6, 7, 8, 9])

    test2.get_nth_node(10).next = test2.get_nth_node(2)
    assert find_loop(test2) is test2.get_nth_node(2)
