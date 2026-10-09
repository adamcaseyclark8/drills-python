def best_time_to_buy_or_sell_stock(prices):
    if not prices:
        return 0

    profit = 0
    stock_to_buy = prices[0]

    for price in prices[1:]:
        if stock_to_buy > price:
            stock_to_buy = price

        current_profit = price - stock_to_buy

        if current_profit > profit:
            profit = current_profit

    return profit
