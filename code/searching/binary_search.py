def perform_binary_search(array, number):
    def search(numbers, target, left, right):
        if left > right:
            return -1

        middle = (left + right) // 2
        potential = numbers[middle]

        if target == potential:
            return middle
        elif target > potential:
            return search(numbers, target, middle + 1, right)
        else:
            return search(numbers, target, left, middle - 1)

    return search(array, number, 0, len(array) - 1)
