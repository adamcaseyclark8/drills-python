def get_nth_fibonacci(nth):
    last_two = [0, 1]
    counter = 3
    while counter <= nth:
        last_two[0], last_two[1] = last_two[1], last_two[0] + last_two[1]
        counter += 1
    return last_two[1] if nth > 1 else last_two[0]
