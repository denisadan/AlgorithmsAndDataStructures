# FIFO
# FirstInFirstOut
# implement a queue with methods: pop, push, peek, getAll
# implement it using a List and a Deque

from collections import deque


class Queue:

    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop(0)

    def peek(self):
        return self.items[0]


class QueueDeque:

    def __init__(self) -> None:
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.popleft()

    def peek(self):
        return self.items[0]
