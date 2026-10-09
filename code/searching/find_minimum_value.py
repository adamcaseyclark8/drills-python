def find_minimum_value(array):
    # Assume the first element is the minimum
    minimum = array[0]
    for value in array[1:]:
        if value < minimum:
            # Update minimum if a smaller value is found
            minimum = value
    return minimum
