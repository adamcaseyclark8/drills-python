def find_duplicate_number(nums):
    seen = set()
    duplicates = {}

    for num in nums:
        if num in seen:
            duplicates[num] = True
        else:
            seen.add(num)

    return list(duplicates)
