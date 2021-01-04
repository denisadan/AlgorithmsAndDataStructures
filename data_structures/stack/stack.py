# LIFO
# LastInFirstOut
# implement a stack with methods: pop, push, peek, isEmpty, size, getAll, add 2 stacks together, comparison of stacks
from collections import deque


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def getAllItems(self):
        return self.items

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __add__(self, other):
        new_stack = Stack()
        new_stack = self.items + other.items
        return new_stack

    def __gt__(self, second_stack):
        return len(self.items) > len(second_stack.items)

    def __ge__(self, second_stack):
        return len(self.items) >= len(second_stack.items)

    def __lt__(self, second_stack):
        return len(self.items) < len(second_stack.items)

    def __le__(self, second_stack):
        return len(self.items) <= len(second_stack.items)


class StackDeque:
    def __init__(self) -> None:
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
