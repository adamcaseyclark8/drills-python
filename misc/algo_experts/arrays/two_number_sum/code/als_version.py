def two_sum(arr, smaller_target_sum, start):
    x = {}
    for i in range(start, len(arr)):
        num = arr[i]
        if x.get(num):
            return True
        x[smaller_target_sum - num] = True
    return False
