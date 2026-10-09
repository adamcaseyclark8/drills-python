# AS EVERY COUNTER += 1,


def sort_via_bubble_sort(array):
    is_sorted = False
    counter = 0

    while not is_sorted:
        is_sorted = True

        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
        counter += 1
    return array


def swap(first, second, array):
    array[first], array[second] = array[second], array[first]
