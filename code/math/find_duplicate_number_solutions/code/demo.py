def find_duplicate_number(numbers):
    duplicates = []
    seen = set()

    for number in numbers:
        if number in seen:
            duplicates.append(number)
        seen.add(number)

    return len(duplicates) or -1
