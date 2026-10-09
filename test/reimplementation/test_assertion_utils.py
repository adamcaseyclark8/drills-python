import pytest

from code.reimplementation.assertion_utils import AssertionUtils


class TestAssertEquals:
    def test_passes_when_values_are_equal(self):
        AssertionUtils.assert_equals('Adam', 'Adam', 'Names match')

    def test_raises_when_values_are_not_equal(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_equals('cat', 'dog', 'Should fail')


class TestAssertTrue:
    def test_passes_when_condition_is_true(self):
        AssertionUtils.assert_true(5 > 3, '5 is greater than 3')

    def test_raises_when_condition_is_false(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_true(2 > 10, 'Should fail')


class TestAssertFalse:
    def test_passes_when_condition_is_false(self):
        AssertionUtils.assert_false(2 > 10, '2 is not greater than 10')

    def test_raises_when_condition_is_true(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_false(5 > 3, 'Should fail')


class TestAssertIsNone:
    def test_passes_when_value_is_none(self):
        AssertionUtils.assert_is_none(None, 'Value is None')

    def test_raises_when_value_is_not_none(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_is_none('hello', 'Should fail')


class TestAssertIsNotNone:
    def test_passes_when_value_is_not_none(self):
        AssertionUtils.assert_is_not_none('hello', 'Value is not None')

    def test_raises_when_value_is_none(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_is_not_none(None, 'Should fail')


class TestAssertNotEquals:
    def test_passes_when_values_are_not_equal(self):
        AssertionUtils.assert_not_equals('cat', 'dog', 'Values differ')

    def test_raises_when_values_are_equal(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_not_equals('cat', 'cat', 'Should fail')


class TestAssertContains:
    def test_passes_when_string_contains_substring(self):
        AssertionUtils.assert_contains('hello world', 'world', 'Contains world')

    def test_raises_when_string_does_not_contain_substring(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_contains('hello world', 'cats', 'Should fail')


class TestAssertArrayEquals:
    def test_passes_when_arrays_are_equal(self):
        AssertionUtils.assert_array_equals([1, 2, 3], [1, 2, 3], 'Arrays match')

    def test_raises_when_array_lengths_differ(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_array_equals([1, 2], [1, 2, 3], 'Should fail')

    def test_raises_when_array_values_differ(self):
        with pytest.raises(AssertionError, match='FAIL'):
            AssertionUtils.assert_array_equals([1, 2, 3], [1, 2, 9], 'Should fail')
