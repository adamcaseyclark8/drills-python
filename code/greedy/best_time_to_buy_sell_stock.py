def best_time_to_buy_sell_stock(numbers):
    min_price = float('inf')
    result = 0

    for number in numbers:
        if number < min_price:
            min_price = number
        elif number - min_price > result:
            result = number - min_price

    return result
