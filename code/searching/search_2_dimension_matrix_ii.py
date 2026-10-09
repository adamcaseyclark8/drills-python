# integers in each row are sorted in ascending order.
# the first integer of each row is greater than the last integer of the previous row.


def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return True
        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
