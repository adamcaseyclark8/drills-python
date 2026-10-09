def two_number_sum_using_map(numbers, target):
    seen = {}
    for i, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], i]
        seen[number] = i
    return None
