def three_number_sum(arr, target_sum):
    def two_sum(smaller_target_sum, start):
        x = {}
        for i in range(start, len(arr)):
            num = arr[i]
            if num is None:
                continue
            if x.get(num):
                return True
            x[smaller_target_sum - num] = True
        return False

    for i in range(len(arr) - 2):
        if arr[i] is None:
            continue
        # print(two_sum(target_sum - arr[i], i + 1))

        if two_sum(target_sum - arr[i], i + 1):
            return True
    return False
