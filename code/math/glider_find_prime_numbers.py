def is_number_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return 'No'

    # 2 is the only even prime number
    if num == 2:
        return 'Yes'

    # Even numbers greater than 2 are not prime
    if num % 2 == 0:
        return 'No'

    # Check for divisibility from 3 up to the square root of the number,
    # incrementing by 2 to only check odd divisors
    i = 3
    while i * i <= num:
        if num % i == 0:
            return 'No'  # Found a divisor, so it's not prime
        i += 2

    return 'Yes'  # No divisors found, so it's prime


# print(is_number_prime(99))
