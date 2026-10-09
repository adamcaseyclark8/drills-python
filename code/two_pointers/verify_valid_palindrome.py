import re


def verify_valid_palindrome(s):
    if not s:
        return False

    # Clean the string: remove non-alphanumeric chars and lowercase
    cleaned = re.sub(r'[^0-9a-zA-Z]', '', s).lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True
