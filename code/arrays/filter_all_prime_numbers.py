import math


def filter_all_prime_numbers(array):
    def is_prime_number(number):
        if number < 2:
            return False
        for i in range(2, math.isqrt(number) + 1):
            if number % i == 0:
                return False
        return True

    return [number for number in array if is_prime_number(number)]
