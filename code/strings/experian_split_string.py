# from chatgpt


def experian_split_string_function(string, interval):
    if len(string) % interval != 0:
        return f'string is not divisible by {interval}'

    result = []
    for i in range(0, len(string), interval):
        result.append(string[i:i + interval])
    return result
