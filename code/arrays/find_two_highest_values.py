def find_two_highest_values(numbers):
    highest = float('-inf')
    second = float('-inf')

    for number in numbers:
        if number > highest:
            second = highest
            highest = number
        elif number > second:
            second = number

    return [highest, second]
