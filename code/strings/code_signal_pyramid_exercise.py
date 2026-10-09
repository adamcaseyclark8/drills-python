# from claude


def build_ascii_pyramid(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)
