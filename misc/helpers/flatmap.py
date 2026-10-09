arr = [1, 2, 3, 4]

x = [[n * 2] for n in arr]
# [[2], [4], [6], [8]]

y = [item for n in arr for item in [n * 2]]
# [2, 4, 6, 8]

# only one level is flattened
z = [item for n in arr for item in [[n * 2]]]
# [[2], [4], [6], [8]]

if __name__ == '__main__':
    print(x)
    print(y)
    print(z)
