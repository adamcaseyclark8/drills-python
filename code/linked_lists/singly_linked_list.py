class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.length += 1
        return node

    def pop(self):
        if not self.head:
            return None

        if not self.head.next:
            node = self.head
            self.head = None
            self.length -= 1
            return node

        current = self.head
        while current.next.next:
            current = current.next
        node = current.next
        current.next = None
        self.length -= 1
        return node

    def delete(self, value):
        if not self.head:
            return None

        if self.head.value == value:
            node = self.head
            self.head = self.head.next
            self.length -= 1
            return node

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            node = current.next
            current.next = current.next.next
            self.length -= 1
            return node

        return None  # value not found

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def to_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.value)
            current = current.next
        return arr
