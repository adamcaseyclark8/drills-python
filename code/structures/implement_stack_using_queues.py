from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # push: enqueue to queue2, then rotate so newest element is always at the front
    def push(self, val):
        self.queue2.append(val)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    # pop: dequeue from the front of queue1 (which holds the top of stack)
    def pop(self):
        if self.is_empty():
            return None
        return self.queue1.popleft()

    # peek: look at the front of queue1 without removing
    def peek(self):
        if self.is_empty():
            return None
        return self.queue1[0]

    def is_empty(self):
        return len(self.queue1) == 0

    def size(self):
        return len(self.queue1)
