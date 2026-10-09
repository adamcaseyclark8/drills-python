def find_duplicate_number(nums):
    duplicates = []
    seen = {}
    for num in nums:
        if seen.get(num):
            duplicates.append(num)
        seen[num] = True
    return duplicates if duplicates else -1  # return -1 if no duplicate found
