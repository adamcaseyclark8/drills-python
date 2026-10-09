def longest_unique_substring(string):
    seen = set()
    left = 0
    longest = ''

    for right in range(len(string)):
        while string[right] in seen:
            seen.remove(string[left])
            left += 1
        seen.add(string[right])
        if right - left + 1 > len(longest):
            longest = string[left:right + 1]
    return longest
