def insertion_sort(array):
    for i in range(1, len(array)):
        j = i

        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)

            j -= 1
    return array


def swap(first, second, array):
    array[first], array[second] = array[second], array[first]
