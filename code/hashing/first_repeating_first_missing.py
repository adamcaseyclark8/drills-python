def first_repeating_first_missing(numbers):
    number_set = set(numbers)
    seen = set()
    repeating = -1
    missing = len(numbers) + 1

    # finds first repeating
    for number in numbers:
        if number in seen:
            repeating = number
            break
        seen.add(number)

    # calculates first missing
    for i in range(1, len(numbers) + 1):
        if i not in number_set:
            missing = i
            break

    return [repeating, missing]
