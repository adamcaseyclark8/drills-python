import pytest

from code.structures.priority_queue.queue import Queue

# IMPLEMENT QUEUE METHODS:
# ENQUEUE, DEQUEUE, PEEK, TO ARRAY


@pytest.fixture
def queue():
    return Queue()


def test_enqueue_adds_elements_to_the_end(queue):
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    assert queue.to_array() == ['a', 'b', 'c']


def test_dequeue_removes_and_returns_elements_in_fifo_order(queue):
    queue.enqueue('first')
    queue.enqueue('second')
    queue.enqueue('third')
    assert queue.dequeue() == 'first'
    assert queue.dequeue() == 'second'
    assert queue.dequeue() == 'third'
    assert queue.dequeue() is None


def test_peek_returns_the_front_element_without_removing_it(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    assert queue.size() == 2


def test_is_empty_works_correctly(queue):
    assert queue.is_empty() is True
    queue.enqueue(5)
    assert queue.is_empty() is False


def test_size_returns_correct_number_of_elements(queue):
    assert queue.size() == 0
    queue.enqueue('x')
    queue.enqueue('y')
    assert queue.size() == 2
    queue.dequeue()
    assert queue.size() == 1


def test_dequeue_on_empty_queue_returns_none(queue):
    assert queue.dequeue() is None


def test_peek_on_empty_queue_returns_none(queue):
    assert queue.peek() is None


def test_to_array_returns_correct_array_representation(queue):
    queue.enqueue('alpha')
    queue.enqueue('beta')
    assert queue.to_array() == ['alpha', 'beta']
