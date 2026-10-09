def detect_loop_in_a_linked_list(head):
    seen = set()

    while head is not None:
        # if this node is already present
        # in hashmap it means there is a cycle
        if head in seen:
            return True

        # if we are seeing the node for
        # the first time, insert it in hash
        seen.add(head)

        head = head.next
    return False
