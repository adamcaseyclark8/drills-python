def two_number_sum_using_set(numbers, target_sum):
    seen = set()
    results = []

    for number in numbers:
        match = target_sum - number
        if match in seen:
            results.append([match, number])
        seen.add(number)

    return results
