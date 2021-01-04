# insertion sort - deck of cards
# 9, 13, 10, 7, 15, 17, 21, 25, 19, 22
# 7 9 10 13 15 17 19 21 22 25

# selection sort
# 9, 13, 10, 7, 15, 17, 21, 25, 19, 22
# 7         9, 13, 10, 15, 17, 21, 25, 19, 22
# 7 9       13, 10, 15, 17, 21, 25, 19, 22
# 7 9 10       13, 15, 17, 21, 25, 19, 22
# 7 9 10 13      15, 17, 21, 25, 19, 22
# .......
# 7 9 10 13 15 17 19            21 22
# 7 9 10 13 15 17 19 21 22           22

# merge sort
# 9, 13, 10, 7, 15, 17, 21, 25, 19, 22
# 9, 13, 10, 7, 15   17, 21, 25, 19, 22
# 9, 13,   10, 7,   15   17, 21,   25, 19,   22

# 9,   13,   10, 7,   15   17,   21,   25,  19,   22

# 9, 13    7, 10    15   17,   21, 25,  19, 22
# 7, 9, 10, 13    15 17,21, 25   19, 22
# 7,9,10,13, 15 17,21, 25   19, 22

# 7,9,10,13, 15 17, 19, 21, 22, 25

#  O(log n)
#  O(n*log n)

def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]  # valoarea curenta
        left_i = i - 1      # indexul elementului din stanga
        while left_i >= 0:
            if array[left_i] > current:
                array[left_i + 1] = array[left_i]    # shiftarea elementului din stanga in dreapta
                array[left_i] = current              # se inlocuieste elementul din stanga cu valoarea curenta
                left_i = left_i - 1                  # mergem spre stanga
            else:
                break


array = [1, 5, 3, 7, 4, 4, 6, 2, 10]
insertion_sort(array)
print(f"Sorted array: {array}")
