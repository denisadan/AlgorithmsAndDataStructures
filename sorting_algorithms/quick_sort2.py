from typing import List


def quick_sort(sir: List[int], low: int, high: int):
    if low < high:
        i = partition(sir, low, high)
        quick_sort(sir, low, i - 1)
        quick_sort(sir, i + 1, high)
    print(f"{sir}")


def partition(sir, low, high):
    start = low
    end = high
    pivot = sir[0]
    while start < end:
        while sir[start] <= pivot:
            start = start + 1
        while sir[end] > pivot:
            end = end - 1

        if start < end:
            sir[start], sir[end] = sir[end], sir[start]

        sir[low], sir[end] = sir[end], sir[low]

    return end


if __name__ == '__main__':
    l = [13, 6, 7, 1,80, 1]
    quick_sort(l, 0, len(l) - 1)
