# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  10]
# [1, 2, 5, 7, 9, 11, 33, 67, 88, 99]  33    L : 0 ; R = 9

# [0,  1,  2,  3,  4 ]
# [11, 33, 67, 88, 99]                 33    M: 5  L:5  R:10

# [11, 33, 67]                               M:2;  L:0  R:2
#  12/2 => 6                                 M: 1
#  13/2 => 6

def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if item == array[middle]:
            return print(f"{item} is at position {middle}")
        elif item < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return "Not found"


print(f"{binary_search_iterative([1, 2, 5, 7, 9, 11, 33, 67, 88, 99, 100], 2)}")


def binary_search_recursive(array, item, begin_index, end_index):
    if begin_index <= end_index:
        middle = (begin_index + end_index) // 2

        if array[middle] == item:
            return middle

        if array[middle] < item:
            return binary_search_recursive(array, item, middle + 1, end_index)
        elif array[middle] > item:
            return binary_search_recursive(array, item, begin_index, middle - 1)

    return False


print("44 is at position", binary_search_recursive([10, 14, 19, 26, 27, 31, 33, 35, 42, 44], 44, 0, 9))

