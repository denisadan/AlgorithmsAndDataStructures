import time

from data_structures.queue.queue import Queue, QueueDeque

queue1 = Queue()
queue2 = QueueDeque()

start = time.time()
for i in range(100000):
    queue1.push("ITEM")

for i in range(100000):
    queue1.pop()

stop = time.time()

print(stop - start)

start = time.time()

for i in range(100000):
    queue2.push("ITEM")

for i in range(100000):
    queue2.pop()

stop = time.time()

print(stop - start)
