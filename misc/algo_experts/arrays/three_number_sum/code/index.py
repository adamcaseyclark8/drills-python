def three_number_sum(number_list, target):
    def get_two(numbers, i):
        return numbers[i] + numbers[i + 1]

    def get_three(total_so_far, starting, total):
        for i in range(len(number_list[starting])):
            return total_so_far + number_list[starting + index] == total  # noqa: F821 - unfinished

    for index in range(len(number_list)):
        if get_two(number_list, index):
            return get_three(get_two(number_list, index), index + 2, target)
