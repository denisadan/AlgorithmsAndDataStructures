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