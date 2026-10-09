def product_sum(array, multiplier=1):
    total = 0

    for element in array:
        if isinstance(element, list):
            total += product_sum(element, multiplier + 1)
        else:
            total += element
    return total * multiplier
