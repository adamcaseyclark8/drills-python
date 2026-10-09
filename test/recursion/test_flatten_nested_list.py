from code.recursion.flatten_nested_list import flatten_nested_list


class TestBasicCases:
    def test_already_flat_returns_same_values(self):
        assert flatten_nested_list([1, 2, 3]) == [1, 2, 3]

    def test_one_level_of_nesting(self):
        assert flatten_nested_list([1, [2, 3]]) == [1, 2, 3]

    def test_two_levels_of_nesting(self):
        assert flatten_nested_list([1, [2, [3, 4]]]) == [1, 2, 3, 4]

    def test_deeply_nested(self):
        assert flatten_nested_list([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]


class TestMixedNesting:
    def test_multiple_nested_arrays_at_same_level(self):
        assert flatten_nested_list([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]

    def test_mix_of_flat_and_nested(self):
        assert flatten_nested_list([1, [2, 3], 4, [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]

    def test_strings_and_numbers_mixed(self):
        assert flatten_nested_list([1, ['a', 'b'], [2, ['c']]]) == [1, 'a', 'b', 2, 'c']


class TestEdgeCases:
    def test_empty_array(self):
        assert flatten_nested_list([]) == []

    def test_array_of_empty_arrays(self):
        assert flatten_nested_list([[], [], []]) == []

    def test_nested_empty_arrays(self):
        assert flatten_nested_list([[], [[], []]]) == []

    def test_single_element(self):
        assert flatten_nested_list([42]) == [42]

    def test_does_not_mutate_the_original_array(self):
        nested = [1, [2, 3]]
        flatten_nested_list(nested)
        assert nested == [1, [2, 3]]
