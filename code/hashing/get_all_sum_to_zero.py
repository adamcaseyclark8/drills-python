def get_all_pairs_that_sum_to_zero(array):
    seen = set()
    results = []
    for num in array:
        if -num in seen:
            results.append([min(num, -num), max(num, -num)])
            seen.remove(-num)
        else:
            seen.add(num)
    return results


# def get_all_pairs_that_sum_to_zero(arr):
#     ordered = sorted(arr)
#     results = []
#     left, right = 0, len(ordered) - 1
#     while left < right:
#         total = ordered[left] + ordered[right]
#         if total == 0:
#             results.append([ordered[left], ordered[right]])
#             left += 1
#             right -= 1
#         elif total < 0:
#             left += 1
#         else:
#             right -= 1
#     return results
