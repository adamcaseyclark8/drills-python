def is_palindrome(string):
    reversed_string = ''

    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return string == reversed_string


if __name__ == '__main__':
    print(is_palindrome('hannah'))
