def move_zeroes_right(numbers):
    last_non_zero_found_at = 0

    # Move all non-zero elements to the beginning
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[last_non_zero_found_at] = numbers[i]
            last_non_zero_found_at += 1

    # Fill the rest with zeros
    for i in range(last_non_zero_found_at, len(numbers)):
        numbers[i] = 0

    return numbers  # Or modify the list in-place without returning
