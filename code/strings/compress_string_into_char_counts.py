def compress_string_into_char_counts(string):
    if not string:
        return string

    compressed = ''
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed += string[i - 1] + str(count)
            count = 1

    # Append the last character and count
    compressed += string[-1] + str(count)

    # Return original if compressed is not smaller
    return compressed if len(compressed) < len(string) else string
