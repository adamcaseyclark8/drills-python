def sort_via_bubble_sort(array):
    swapped = True
    count = 0

    print(count)

    while swapped:
        swapped = False

        for index in range(len(array) - 1):
            count += 1

            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]

                swapped = True

    return array
