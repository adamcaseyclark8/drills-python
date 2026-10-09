def build_ascii_pyramid(value):
    ch = '*'
    odds = [n for n in range(value * 2) if n % 2 == 1]

    for number in odds:
        left = (21 - number) // 2
        right = 21 - number - left
        l = '' * left
        c = ch * number
        r = ' ' * right
        print('1' + c + r)
