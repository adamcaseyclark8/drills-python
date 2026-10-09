def find_closest_value_in_bst(tree, target):
    return find_closet_value_in_bst_helper(tree, target, float('inf'))


def find_closet_value_in_bst_helper(tree, target, closest):
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return find_closet_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closet_value_in_bst_helper(tree.right, target, closest)
    else:
        return closest
