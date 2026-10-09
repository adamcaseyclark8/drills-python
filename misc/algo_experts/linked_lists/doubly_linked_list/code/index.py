class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_before(self.head, node)

    def set_tail(self, node):
        if self.tail is None:
            self.set_head(node)
            return
        self.insert_after(self.tail, node)

    def insert_before(self, node, node_to_insert):
        if node_to_insert is self.head and node_to_insert is self.tail:
            return

        self.remove(node_to_insert)
        node_to_insert.previous = node.previous
        node_to_insert.next = node

        if node.previous is None:
            self.head = node_to_insert
        else:
            node.previous.next = node_to_insert
        node.previous = node_to_insert

    def insert_after(self, node, node_to_insert):
        if node_to_insert is self.head and node_to_insert is self.tail:
            return

        self.remove(node_to_insert)
        node_to_insert.previous = node
        node_to_insert.next = node.next

        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.previous = node_to_insert
        node.next = node_to_insert

    def insert_at_position(self, position, node_to_insert):
        if position == 1:
            self.set_head(node_to_insert)
            return

        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            current_position += 1
            node = node.next

            if node is not None:
                self.insert_before(node, node_to_insert)
            else:
                self.set_tail(node_to_insert)

    def remove_nodes_with_value(self, value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    def contains_node_with_value(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def remove(self, node):
        if node is self.head:
            self.head = self.head.next

        if node is self.tail:
            self.tail = self.tail.previous

        self.remove_node_bindings(node)

    def remove_node_bindings(self, node):
        if node.previous is not None:
            node.previous.next = node.next

        if node.next is not None:
            node.next.previous = node.previous

        node.previous = None
        node.next = None
