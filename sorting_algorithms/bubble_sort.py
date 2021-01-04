# 0 1 2 3 4 5  6

# 9 13 10 7 15 17
# 9 10 13 7 15 17
# 9 10 7 13 15 17
# 9 7 10 13 15 17
# 7 9 10 13 15 17

# n = len(sir)
# for i = 0, n-1
#   for j = 0, n - 1
#       if sir[j] > sir [j+1]:
#             swap
import time
from typing import List


def bubble_sort(sir: List[int]):
    n = len(sir)
    already_sorted = True
    for i in range(0, n - 1):
        for j in range(0, n - 1):  # can we optimize more this loop?
            if sir[j] > sir[j + 1]:
                sir[j], sir[j + 1] = sir[j + 1], sir[j]
                already_sorted = False
        if already_sorted: break
    print(f"{sir}")
    return sir


# O(n) * O(n)  = O (n^2)
# O(n) * O(log n) = O(n * logn)

start = time.time()
bubble_sort([9, 13, 10, 7, 15, 17, 21, 25, 19, 22, 33, 40, 41, 1, -10])
# bubble_sort([1, 2, 3, 4, 5, 6, 7])
# print(f"{sorted([1, 2, 3, 4, 5, 6, 7])}")
stop = time.time()
print(f"{stop - start}")
# print(f"{sorted([1, 2, 3, 4, 5, 6, 7])}")
# swap 2 numbers
# a, b
# aux = a; a=b; b = aux
# a,b = b,a


# 7 6 10 5 21 15 8
#   s  e

# 5 6 10 7 21 15 8
