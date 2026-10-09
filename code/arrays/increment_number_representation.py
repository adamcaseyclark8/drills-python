def increment_number_representation(digits):
    result = list(digits)

    # LAST DIGIT IN ARRAY FIRST
    # MOVING LEFT TO RIGHT
    # WHILE INDEX IS GREATER THAN OR EQUAL TO ZERO

    for i in range(len(result) - 1, -1, -1):
        if result[i] < 9:
            result[i] += 1
            return result
        result[i] = 0

    # All digits were 9, prepend a 1
    return [1, *result]
