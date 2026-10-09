class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# helper to build a linked list from an array
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# helper to convert a linked list back to an array (for easy test assertions)
def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# slow/fast pointer technique — when fast reaches the end, slow is at the middle
def find_middle_node(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow
