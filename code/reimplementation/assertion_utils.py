class AssertionUtils:
    @staticmethod
    def assert_equals(expected, actual, message):
        if expected != actual:
            raise AssertionError(f'FAIL - {message}\n  Expected: {expected}\n  Actual:   {actual}')

    @staticmethod
    def assert_true(condition, message):
        if not condition:
            raise AssertionError(f'FAIL - {message} | Expected: true | Actual: false')

    @staticmethod
    def assert_false(condition, message):
        if condition:
            raise AssertionError(f'FAIL - {message} | Expected: false | Actual: true')

    @staticmethod
    def assert_is_none(actual, message):
        if actual is not None:
            raise AssertionError(f'FAIL - {message} | Expected: None | Actual: {actual}')

    @staticmethod
    def assert_is_not_none(actual, message):
        if actual is None:
            raise AssertionError(f'FAIL - {message} | Expected: not None | Actual: None')

    @staticmethod
    def assert_not_equals(expected, actual, message):
        if expected == actual:
            raise AssertionError(f'FAIL - {message} | Values should not be equal: {expected}')

    @staticmethod
    def assert_contains(actual, substring, message):
        if substring not in actual:
            raise AssertionError(f'FAIL - {message}\n  String: {actual}\n  Expected to contain: {substring}')

    @staticmethod
    def assert_array_equals(expected, actual, message):
        if len(expected) != len(actual):
            raise AssertionError(f'FAIL - {message} | Array lengths differ')
        for i in range(len(expected)):
            if expected[i] != actual[i]:
                raise AssertionError(
                    f'FAIL - {message} | Mismatch at index {i} Expected: {expected[i]} Actual: {actual[i]}'
                )
