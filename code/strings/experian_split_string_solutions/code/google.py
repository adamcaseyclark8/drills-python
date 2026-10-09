import math


def experian_split_sting_function(string, interval):
    if len(string) % interval != 0:
        return f'string is not divisible by {interval}'

    num_intervals = math.ceil(len(string) / interval)

    return [string[i * interval:i * interval + interval] for i in range(num_intervals)]
