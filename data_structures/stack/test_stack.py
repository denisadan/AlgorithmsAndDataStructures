import time

from data_structures.stack.stack import Stack, StackDeque

stack1 = Stack()
stack2 = StackDeque()

start = time.time()
for i in range(10000):
    stack1.push("ITEM")

for i in range(10000):
    stack1.pop()

stop = time.time()

print(stop - start)

start = time.time()

for i in range(10000):
    stack2.push("ITEM")

for i in range(10000):
    stack2.pop()

stop = time.time()

print(stop - start)
