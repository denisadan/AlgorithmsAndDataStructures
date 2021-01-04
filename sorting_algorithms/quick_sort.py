# quick sort

# smaller than pivot    pivot   greater than pivot

#                    start = s; end = e
# 7 6 10 5 21 15 8   pivot = 7
# s      e

# 5 6 7 10 21 15 8
#     s          e

# 5 6 7 10 21 15 8
# # # # # # # # # # # # # #

# 13 6 7 1 5 3 4 10 60 29   pivot = 13
#                 e   s

# low                           high
# 10 6 7 1 5 3 4      13     60 29

# s2
# 10 6 7 1 5 3 4   pivot = 10
#              e/s

# s3
# 6 7 1 5 3 4   10
#   s       e
# 4 7 1 5 3 6
#   s       e

# 4 6 1 5 3 7
#         s e


from typing import List


def quick_sort(sir: List[int], low: int, high: int):
    if low < high:
        i = partition(sir, low, high)
        quick_sort(sir, low, i - 1)
        quick_sort(sir, i + 1, high)
    print(f"{sir}")


def partition(sir, low, high):
    pivot = sir[low]  # 7
    start = low  # 0
    end = high  # 6

    while start < end:
        while sir[start] <= pivot:
            start = start + 1
        while sir[end] > pivot:
            end = end - 1

        if start < end:  # 13 6 7 1 5 3 4 10 60 29   pivot = 13
            sir[start], sir[end] = sir[end], sir[start]  # e    s;   cand start depaseste end nu mai facem swap

    sir[low], sir[end] = sir[end], sir[low]  # pun pivotul in pozitia potrivita

    return end


if __name__ == '__main__':
    l = [7, 6, 10, 5, 21, 1, 11, 99, 5]
    quick_sort(l, 0, len(l) - 1)
