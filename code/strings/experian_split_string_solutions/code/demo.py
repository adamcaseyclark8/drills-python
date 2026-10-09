def experian_split_sting_function(string, interval):
    result = []
    if len(string) % interval != 0:
        return f'string is not divisible by {interval}'

    for start in range(0, len(string), interval):
        # print(start, start + interval)

        # 03 47

        result.append(string[start:start + interval])

    return result


# experian_split_sting_function('adamcaseyclarkxx', 4)
# print(experian_split_sting_function('adamcaseyclarkxx', 4))
