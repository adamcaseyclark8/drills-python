import pytest

from code.structures.implement_stack_using_queues import StackUsingQueues

# IMPLEMENT STACK METHODS:
# PUSH, POP, PEEK, IS EMPTY, SIZE


@pytest.fixture
def stack():
    return StackUsingQueues()


class TestPushAndPop:
    def test_push_one_item_and_pop_it(self, stack):
        stack.push(1)
        assert stack.pop() == 1

    def test_push_multiple_items_pops_in_lifo_order(self, stack):
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_pop_on_empty_stack_returns_none(self, stack):
        assert stack.pop() is None

    def test_pop_reduces_size(self, stack):
        stack.push(1)
        stack.push(2)
        stack.pop()
        assert stack.size() == 1


class TestPeek:
    def test_peek_returns_top_element_without_removing_it(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.size() == 2

    def test_peek_on_empty_stack_returns_none(self, stack):
        assert stack.peek() is None

    def test_peek_reflects_latest_push(self, stack):
        stack.push(10)
        assert stack.peek() == 10
        stack.push(20)
        assert stack.peek() == 20


class TestIsEmpty:
    def test_new_stack_is_empty(self, stack):
        assert stack.is_empty() is True

    def test_not_empty_after_push(self, stack):
        stack.push(1)
        assert stack.is_empty() is False

    def test_empty_again_after_popping_all_elements(self, stack):
        stack.push(1)
        stack.push(2)
        stack.pop()
        stack.pop()
        assert stack.is_empty() is True


class TestSize:
    def test_size_starts_at_0(self, stack):
        assert stack.size() == 0

    def test_size_increments_with_each_push(self, stack):
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.size() == 3

    def test_size_decrements_with_each_pop(self, stack):
        stack.push(1)
        stack.push(2)
        stack.pop()
        assert stack.size() == 1


class TestInterleavedPushAndPop:
    def test_push_pop_push_pop_maintains_correct_order(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 1

    def test_alternating_pushes_and_peeks(self, stack):
        stack.push(5)
        assert stack.peek() == 5
        stack.push(10)
        assert stack.peek() == 10
        stack.pop()
        assert stack.peek() == 5
