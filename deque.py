# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.
# Adrianna Gilmore

# Hint: pip3 install llist
from llist import dllist

class Deque:

    def __init__(self):
        self.data = dllist()
        self.length = 0

    def enqueue_left(self, value):
        self.data.appendleft(value)
        self.length += 1
    
    def enqueue_right(self, value):
        self.data.append(value)
        self.length += 1

    def dequeue_left(self):
        self.length -= 1
        return self.data.popleft()

    def dequeue_right(self):
        self.length -= 1
        return self.data.pop()

    def is_empty(self):
        return self.length == 0