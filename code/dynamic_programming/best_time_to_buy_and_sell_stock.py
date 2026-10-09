def best_time_to_buy_and_sell_stock(prices):
    if not prices or len(prices) < 2:
        return 0

    minimum = prices[0]
    maximum = 0

    for i in range(1, len(prices)):
        minimum = min(minimum, prices[i])
        maximum = max(maximum, prices[i] - minimum)

    return maximum
