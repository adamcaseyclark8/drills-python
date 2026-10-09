def move_element_to_end(array):
    count = 0
    for num in array:
        if num == 0:
            array[count] = array[count + 1]
            array[count] = array[count + 1]
            count += 1
    return array
