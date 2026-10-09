def is_palindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and is_palindrome(string, i + 1)


if __name__ == '__main__':
    print(is_palindrome('hannah'))
