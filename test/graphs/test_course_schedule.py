from code.graphs.course_schedule import can_finish_courses


def test_returns_true_when_no_prerequisites():
    assert can_finish_courses(3, []) is True


def test_returns_true_for_simple_valid_dependency_chain():
    num_courses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    # Order: 0 -> 1 -> 2 -> 3
    assert can_finish_courses(num_courses, prerequisites) is True


def test_returns_false_for_simple_cycle():
    num_courses = 2
    prerequisites = [[0, 1], [1, 0]]
    # Cycle: 0 -> 1 -> 0
    assert can_finish_courses(num_courses, prerequisites) is False


def test_returns_false_for_larger_cycle():
    num_courses = 4
    prerequisites = [[1, 0], [2, 1], [0, 2]]
    # Cycle: 0 -> 1 -> 2 -> 0
    assert can_finish_courses(num_courses, prerequisites) is False


def test_returns_true_for_multiple_independent_chains():
    num_courses = 6
    prerequisites = [
        [1, 0],  # chain 1: 0 -> 1
        [3, 2],  # chain 2: 2 -> 3
        [5, 4],  # chain 3: 4 -> 5
    ]
    assert can_finish_courses(num_courses, prerequisites) is True


def test_returns_true_for_complex_valid_graph_with_branches():
    num_courses = 5
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]
    # Valid order exists: 0 -> 1/2 -> 3 -> 4
    assert can_finish_courses(num_courses, prerequisites) is True


def test_returns_false_when_single_course_depends_on_itself():
    assert can_finish_courses(1, [[0, 0]]) is False


def test_handles_disconnected_graph_with_one_cycle():
    num_courses = 5
    prerequisites = [
        [1, 0],
        [2, 1],
        [0, 2],  # cycle in subgraph
        [4, 3],  # separate valid subgraph
    ]
    assert can_finish_courses(num_courses, prerequisites) is False
