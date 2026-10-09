def vail_stock_problem(numbers):
    profits = []
    current = numbers[0] if numbers else None

    for i in range(len(numbers)):
        if isinstance(numbers[i], str):
            return 'all values must be numeric'

        if numbers[i] < 0:
            return 'all values must be positive'

        if i > 0 and numbers[i - 1] > numbers[i]:
            profits.append(numbers[i - 1] - current)
            current = numbers[i]
        elif i == len(numbers) - 1:
            profits.append(numbers[i] - current)

    return sum(profits)


# print(vail_stock_problem([500, 750, 1000, 200, 1200, 300, 500]))
# print(vail_stock_problem([500, 300, 1000, 100, 1200, 400, 500]))
# print(vail_stock_problem([500, 400, 300, 200, 100]))
# print(vail_stock_problem([1500, 'two', 300, 200, 100]))
# print(vail_stock_problem([500, -750, 1000, 200, 1200, 300, 500]))
# print(vail_stock_problem([]))
# print(vail_stock_problem([500]))
# print(vail_stock_problem([500, 1300]))
