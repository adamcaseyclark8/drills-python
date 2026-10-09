from code.backtracking.permutations_of_an_array import permutations_of_an_array


# Helper: sort a list of arrays for order-independent comparison
def sort(arrays):
    return sorted(list(p) for p in arrays)


def test_empty_array_returns_one_empty_permutation():
    assert permutations_of_an_array([]) == [[]]


def test_single_element_returns_one_permutation():
    assert permutations_of_an_array([1]) == [[1]]


def test_two_elements_returns_2_permutations():
    assert sort(permutations_of_an_array([1, 2])) == sort([[1, 2], [2, 1]])


def test_three_elements_returns_6_permutations():
    result = permutations_of_an_array([1, 2, 3])

    # Correct count: 3! = 6
    assert len(result) == 6

    # Contains every expected arrangement
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sort(result) == sort(expected)


def test_four_elements_returns_24_permutations():
    assert len(permutations_of_an_array([1, 2, 3, 4])) == 24  # 4! = 24


def test_no_duplicate_permutations_are_produced():
    result = permutations_of_an_array([1, 2, 3])
    unique = {tuple(p) for p in result}
    assert len(unique) == len(result)


def test_each_permutation_contains_all_original_elements():
    numbers = [4, 5, 6]
    for perm in permutations_of_an_array(numbers):
        assert sorted(perm) == sorted(numbers)


def test_works_with_non_numeric_values():
    result = permutations_of_an_array(['a', 'b', 'c'])
    assert len(result) == 6
    assert ['a', 'b', 'c'] in result
    assert ['c', 'b', 'a'] in result


def test_does_not_mutate_the_input_array():
    numbers = [1, 2, 3]
    copy = list(numbers)
    permutations_of_an_array(numbers)
    assert numbers == copy
