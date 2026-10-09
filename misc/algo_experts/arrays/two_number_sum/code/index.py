# v1 - time: O(n^2) | space: O(1)
# runs first element in parent array
# loops all in nested array
# stops after it finds

# def two_number_sum(array, target_sum):
#     for i in range(len(array) - 1):
#         first_num = array[i]
#
#         print('first_num')
#         print(first_num)
#
#         for j in range(i + 1, len(array)):
#             second_num = array[j]
#
#             print('second_num')
#             print(second_num)
#
#             if first_num + second_num == target_sum:
#                 return [first_num, second_num]
#     return []

# v2 - time: O(n) | space: O(n)
# loops over array subtracts element from target


def two_number_sum(array, target_sum):
    nums = {}
    for num in array:
        potential_match = target_sum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True

    return []


# v3 - time: O(nlog(n)) | space: O(1)

# def two_number_sum(array, target_sum):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#
#     while left < right:
#         current_sum = array[left] + array[right]
#         if current_sum == target_sum:
#             return [array[left], array[right]]
#         elif current_sum < target_sum:
#             left += 1
#         elif current_sum > target_sum:
#             right -= 1
#     return []
