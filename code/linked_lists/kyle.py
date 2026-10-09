class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_node(value):
    return Node(value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = create_node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return node

        self.tail.next = node
        self.tail = node
        self.length += 1

        return node

    def pop(self):
        if self.is_empty():
            return None

        node = self.tail

        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return node

        current = self.head
        penultimate = None
        while current:
            if current.next is self.tail:
                penultimate = current
                break

            current = current.next

        penultimate.next = None
        self.tail = penultimate
        self.length -= 1

        return node

    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None

        if index == 0:
            return self.head

        current = self.head
        i = 0
        while i < index:
            i += 1
            current = current.next

        return current

    def delete(self, index):
        if index < 0 or index > self.length - 1:
            return None

        if index == 0:
            deleted = self.head

            self.head = self.head.next
            self.length -= 1

            return deleted

        current = self.head
        previous = None
        i = 0

        while i < index:
            i += 1
            previous = current
            current = current.next

        deleted = current
        previous.next = current.next

        if previous.next is None:
            self.tail = previous

        self.length -= 1

        return deleted

    def is_empty(self):
        return self.length == 0

    def print(self):
        values = []
        current = self.head

        while current:
            values.append(str(current.value))
            current = current.next

        return ' => '.join(values)


def create_linked_list():
    return LinkedList()
