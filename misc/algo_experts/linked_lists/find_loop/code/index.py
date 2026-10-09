class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_loop(head):
    first = head.next
    second = head.next.next

    while first is not second:
        first = first.next
        second = second.next.next
    first = head

    while first is not second:
        first = first.next
        second = second.next
    return first
