import pytest

from code.structures.priority_queue.priority_queue import PriorityQueue


@pytest.fixture
def pq():
    return PriorityQueue()


def test_enqueue_and_dequeue_single_item(pq):
    pq.enqueue('task1', 1)
    assert pq.dequeue() == 'task1'
    assert pq.is_empty() is True


def test_items_are_dequeued_by_priority_min_priority(pq):
    pq.enqueue('low', 5)
    pq.enqueue('medium', 3)
    pq.enqueue('high', 1)
    assert pq.dequeue() == 'high'
    assert pq.dequeue() == 'medium'
    assert pq.dequeue() == 'low'


def test_peek_returns_item_with_highest_priority_without_removing(pq):
    pq.enqueue('A', 10)
    pq.enqueue('B', 5)
    assert pq.peek() == 'B'
    assert pq.size() == 2


def test_is_empty_works_correctly(pq):
    assert pq.is_empty() is True
    pq.enqueue('X', 1)
    assert pq.is_empty() is False


def test_size_reflects_correct_number_of_elements(pq):
    assert pq.size() == 0
    pq.enqueue('task1', 2)
    pq.enqueue('task2', 3)
    assert pq.size() == 2
    pq.dequeue()
    assert pq.size() == 1


def test_handles_dequeue_on_empty_queue_gracefully(pq):
    assert pq.dequeue() is None


def test_handles_peek_on_empty_queue_gracefully(pq):
    assert pq.peek() is None


def test_can_enqueue_multiple_items_with_same_priority(pq):
    pq.enqueue('A', 2)
    pq.enqueue('B', 2)
    pq.enqueue('C', 1)
    assert pq.dequeue() == 'C'
    rest = [pq.dequeue(), pq.dequeue()]
    assert 'A' in rest
    assert 'B' in rest


def test_maintains_correct_ordering_after_interleaved_operations(pq):
    pq.enqueue('task1', 4)
    pq.enqueue('task2', 2)
    assert pq.dequeue() == 'task2'
    pq.enqueue('task3', 1)
    assert pq.dequeue() == 'task3'
    assert pq.dequeue() == 'task1'
    assert pq.is_empty() is True
