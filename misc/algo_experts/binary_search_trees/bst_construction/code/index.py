class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parent_node=None):
        current_node = self

        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.right
                        current_node.right = current_node.right.right
                    else:
                        current_node.value = None
                elif parent_node.left is current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right is current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.value


# replace remove value and replace it with smallest value of the right subtree
# delete the smallest value of the right subtree
#

# average: time & space O(log(n)) -> n is number of nodes
# worst: time &  O(n)
# frames on the call stack
