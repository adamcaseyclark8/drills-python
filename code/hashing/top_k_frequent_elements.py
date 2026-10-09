def get_top_k_frequent_elements(nums, k):
    frequency_map = {}

    # Step 1: Count frequencies
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Step 2: Bucket sort - array index represents frequency
    bucket = [[] for _ in range(len(nums) + 1)]

    # [5, 3, 1, 1, 1, 3, 5, 5, 5]
    # {5: 4, 1: 3, 3: 2}
    # [[],[],[3],[1],[5],[],[],[],[]]

    for num, freq in frequency_map.items():
        bucket[freq].append(num)

    # Step 3: Collect top k frequent elements
    result = []

    for i in range(len(bucket) - 1, -1, -1):
        if len(result) >= k:
            break
        if bucket[i]:
            result.extend(bucket[i])

    return result[:k]  # in case more than k elements were added


# get_top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2)
# get_top_k_frequent_elements([8, 8, 8, 9, 9, 10, 10, 6, 6, 6, 6, 6, 7], 2)
