def implement_deep_equals_comparison(a, b):
    # 1. Identity check for same object references
    if a is b:
        return True

    # 2. Handle primitives (and None): same type and same value
    if not isinstance(a, (list, dict)) or not isinstance(b, (list, dict)):
        return type(a) is type(b) and a == b

    # 3. Handle lists
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not implement_deep_equals_comparison(a[i], b[i]):
                return False
        return True

    # 4. Handle dicts
    if isinstance(a, list) != isinstance(b, list):
        # One is a list, other is not
        return False

    if len(a) != len(b):
        return False

    for key in a:
        if key not in b or not implement_deep_equals_comparison(a[key], b[key]):
            return False

    return True
