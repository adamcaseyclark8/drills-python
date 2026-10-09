def get_minimum_window_substring(s, t):
    if not s or not t:
        return ''

    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    left = 0
    formed = 0
    min_len = float('inf')
    min_start = 0
    window = {}

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1

        if c in need and window[c] == need[c]:
            formed += 1

        while formed == len(need):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return '' if min_len == float('inf') else s[min_start:min_start + min_len]
