from code.greedy.perform_activity_selection import perform_activity_selection


def test_returns_maximum_non_overlapping_activities():
    activities = [
        {'start': 1, 'end': 4},
        {'start': 3, 'end': 5},
        {'start': 0, 'end': 6},
        {'start': 5, 'end': 7},
        {'start': 3, 'end': 9},
        {'start': 6, 'end': 10},
        {'start': 8, 'end': 11},
        {'start': 8, 'end': 12},
        {'start': 2, 'end': 14},
        {'start': 12, 'end': 16},
    ]
    assert len(perform_activity_selection(activities)) == 4


def test_single_activity_returns_itself():
    assert perform_activity_selection([{'start': 1, 'end': 2}]) == [{'start': 1, 'end': 2}]


def test_non_overlapping_activities_returns_all():
    activities = [{'start': 1, 'end': 2}, {'start': 3, 'end': 4}, {'start': 5, 'end': 6}]
    assert len(perform_activity_selection(activities)) == 3


def test_all_overlapping_returns_only_one():
    activities = [{'start': 1, 'end': 10}, {'start': 2, 'end': 9}, {'start': 3, 'end': 8}]
    assert len(perform_activity_selection(activities)) == 1


def test_does_not_mutate_input():
    activities = [{'start': 3, 'end': 5}, {'start': 1, 'end': 4}]
    copy = list(activities)
    perform_activity_selection(activities)
    assert activities == copy


def test_adjacent_activities_are_selected():
    activities = [{'start': 0, 'end': 2}, {'start': 2, 'end': 4}, {'start': 4, 'end': 6}]
    assert len(perform_activity_selection(activities)) == 3
