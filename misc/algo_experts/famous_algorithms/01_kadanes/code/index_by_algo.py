def kadanes(array):
    max_ending_here = array[0]
    max_so_far = array[0]

    for num in array[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
