import copy
import heapq
import math
import random
import time
from typing import List, Callable, Union

import matplotlib.pyplot as plt


def get_times(arrays: List[List[int]], sort_function: Callable[[List[int]], List[int]]) -> List[float]:
    temp_lists = copy.deepcopy(arrays)
    times = []
    for temp_list in temp_lists:
        start_time = time.time()
        sort_function(temp_list)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


def get_random_lists(lengths_of_lists: List[int]) -> List[List[int]]:
    random_lists = []
    for length in lengths_of_lists:
        random_lists.append([random.randint(0, 100) for _ in range(length)])
    return random_lists


def bubble_sort(sir: List[int]) -> List[int]:
    n = len(sir)
    already_sorted = True
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if sir[j] > sir[j + 1]:
                sir[j], sir[j + 1] = sir[j + 1], sir[j]
                already_sorted = False
        if already_sorted: break
    return sir


def quick_sort(lst: List[int], low: int = 0, high: Union[None, int] = None) -> List[int]:
    if high is None:
        high = len(lst) - 1

    if low < high:
        # pi is partitioning index
        i = (low - 1)  # index of smaller element
        pivot = lst[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if lst[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        pi = i + 1

        # Separately sort elements before
        # partition and after partition
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)

    return lst


def partition(list, lowerBound, upperBound, pivot):
    start = lowerBound
    end = lowerBound
    while start < end:
        while list[lowerBound] < pivot:
            start = start + 1

        while list[upperBound] > pivot:
            end = end - 1
        if start < end:
            list[start], list[end] = list[end], list[start]
    list[lowerBound], list[end] = list[end], list[lowerBound]
    return end


def heap_sort(lst: List[int]) -> List[int]:
    h = []
    for value in lst:
        heapq.heappush(h, value)
        return [heapq.heappop(h) for i in range(len(h))]


def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        current = array[i]
        left_i = i - 1
        while left_i >= 0:
            if array[left_i] > current:
                array[left_i + 1] = array[left_i]
                array[left_i] = current
                left_i = left_i - 1
            else:
                break
    return array


def split(list):
    list_of_lists = []
    for split in range(0, len(list), 1):
        list_of_lists.append(list[split:split + 1])

    return list_of_lists


def merge(a, b):
    c = []
    while (len(a) > 0) and (len(b) > 0):
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) > 0:
        c.extend(a)
    if len(b) > 0:
        c.extend(b)
    return c


def merge_sort(list_of_lists):
    list_of_merged_lists = []
    for merge_index in range(0, len(list_of_lists), 2):
        if merge_index + 1 < len(list_of_lists):
            list_of_merged_lists.append(merge(list_of_lists[merge_index], list_of_lists[merge_index + 1]))
        else:
            list_of_merged_lists.append(list_of_lists[merge_index])
    return list_of_merged_lists


def my_merge_sort(array: List[int]) -> List[int]:
    list_of_lists = split(array)

    list_of_merged_lists = []
    n = len(array)
    for i in range(int(math.log(n, 2) + 1)):
        list_of_merged_lists = merge_sort(list_of_lists)
        list_of_lists = list_of_merged_lists

    return list_of_lists[0]


if __name__ == '__main__':
    lengths = [10, 100, 200, 300, 400, 500, 700, 800, 900, 1000]
    lists = get_random_lists(lengths)

    quick_sort_results = get_times(lists, quick_sort)
    bubble_sort_results = get_times(lists, bubble_sort)
    heap_sort_results = get_times(lists, heap_sort)
    insertion_sort_results = get_times(lists, insertion_sort)
    merge_sort_results = get_times(lists, my_merge_sort)

    plt.plot(lengths, quick_sort_results, label='quick')
    plt.plot(lengths, bubble_sort_results, label='bubble')
    plt.plot(lengths, heap_sort_results, label='heap')
    plt.plot(lengths, insertion_sort_results, label='insertion')
    plt.plot(lengths, merge_sort_results, label='merge')
    plt.legend()
    plt.show()
