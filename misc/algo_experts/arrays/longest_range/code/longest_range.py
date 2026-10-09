# hint: how can you use a hash table to solve this problem with an algorithm that runs in linear time?


def longest_range(array):
    best = []
    longest = 0

    nums = {}

    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue
        nums[num] = False

        current = 1
        left = num - 1
        right = num + 1

        while left in nums:
            nums[left] = False
            current += 1
            left -= 1
        while right in nums:
            nums[right] = False
            current += 1
            right += 1
        if current > longest:
            longest = current

            best = [left + 1, right + 1]
        return best
