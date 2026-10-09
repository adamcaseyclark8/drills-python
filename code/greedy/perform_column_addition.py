def perform_column_addition(num1, num2):
    reversed_num1 = num1[::-1]
    reversed_num2 = num2[::-1]
    max_length = max(len(reversed_num1), len(reversed_num2))
    carry = 0
    results = []

    i = 0
    while i < max_length or carry:
        digit1 = int(reversed_num1[i]) if i < len(reversed_num1) else 0
        digit2 = int(reversed_num2[i]) if i < len(reversed_num2) else 0
        total = digit1 + digit2 + carry
        carry = total // 10
        results.append(str(total % 10))
        i += 1

    return ''.join(reversed(results))
