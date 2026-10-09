def is_palindrome(string):
    reversed_chars = []

    for i in range(len(string) - 1, -1, -1):
        reversed_chars.append(string[i])
    return string == ''.join(reversed_chars)


if __name__ == '__main__':
    print(is_palindrome('hannah'))
