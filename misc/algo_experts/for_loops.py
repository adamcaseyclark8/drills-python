# 5 TYPES LOOPING BEYOND STANDARD


def print_header(title):
    print('')
    print('--------------------------------------------------')
    print(title)
    print('--------------------------------------------------')
    print('')


# WHEN INDEX MIMICS COUNTING (TO SEE WHAT IS MISSING)
# STARTS AT 1, NOT ZERO
# USED IN: FIRST REPEATING, FIRST MISSING


def looping_type_one(array):
    for i in range(1, len(array)):
        print(i)


# WHEN STARTING WITH LARGEST TO SMALLEST INDICES ()
# USED IN: STRING A REVERSE (NOT IN PLACE)


def looping_type_two(array):
    for i in range(len(array) - 1, -1, -1):
        print(f'number @ index {i} => {array[i]}')


# NESTED LOOP TO CREATE SMALLER LOOPS STARTING WITH INDEX
# USED IN:


def looping_type_three(array):
    for i in range(len(array)):
        for j in range(i, i + 2):
            print(f'index i => {i}, index j => {j}')


# LOOP THAT INCREMENTS TO LARGER THAN ONE - MAKE LESS THAN LENGTH
# USED IN: SPLIT STRING


def looping_type_four(array, interval):
    for i in range(0, len(array), interval):
        print(f'array @ index {i} => {array[i]}')


# LOOPS THROUGH ENTIRE ARRAY THEN DECREASES THE ARRAY BY 1 FOR EACH OF THE NEXT LOOPS
# USED IN: BUBBLE SORT


def looping_type_five(array):
    count = 0

    while count < 2:
        print(f'count => {count}')
        for i in range(len(array) - count):
            print(f'array @ index {i} => {array[i]}')
        count += 1


if __name__ == '__main__':
    print_header('type 1 loop')
    looping_type_one([1, 2, 3, 4, 5])

    print_header('type 2 loop')
    looping_type_two([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print_header('type 3 loop')
    looping_type_three([1, 2, 3, 4])

    print_header('type 4 loop')
    looping_type_four([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

    print_header('type 5 loop')
    looping_type_five([1, 2, 3, 4])
