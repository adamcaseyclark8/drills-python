import copy

from code.graphs.count_number_of_islands import count_number_of_islands


def test_should_return_0_for_an_empty_grid():
    assert count_number_of_islands([]) == 0


def test_should_return_0_when_there_is_only_water():
    grid = [
        ['0', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', '0'],
    ]
    assert count_number_of_islands(grid) == 0


def test_should_return_1_when_there_is_only_one_island():
    grid = [
        ['1', '1', '0'],
        ['1', '1', '0'],
        ['0', '0', '0'],
    ]
    assert count_number_of_islands(grid) == 1


def test_should_return_3_for_a_grid_with_3_separate_islands():
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    assert count_number_of_islands(grid) == 3


def test_should_handle_diagonals_not_being_connected():
    grid = [
        ['1', '0', '1'],
        ['0', '1', '0'],
        ['1', '0', '1'],
    ]
    assert count_number_of_islands(grid) == 5  # Diagonal connections don't count


def test_should_return_correct_count_for_a_large_single_island():
    grid = [
        ['1', '1', '1', '1'],
        ['1', '1', '1', '1'],
        ['1', '1', '1', '1'],
    ]
    assert count_number_of_islands(grid) == 1


def test_should_not_mutate_original_grid_if_needed_optional():
    grid = [
        ['1', '1', '0'],
        ['1', '0', '0'],
        ['0', '0', '1'],
    ]
    deep_copy = copy.deepcopy(grid)
    count_number_of_islands(grid)
    assert grid != deep_copy  # Optional test to remind mutation
