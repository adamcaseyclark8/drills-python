def longest_sequence_of_numbers(nums):
    set_of_numbers = set(nums)
    longest_sequence = 0

    for num in set_of_numbers:
        if num - 1 not in set_of_numbers:
            current_num = num
            current_sequence = 1

            while current_num + 1 in set_of_numbers:
                current_num += 1
                current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence
