import math


# definim split lista in lista de liste
def split(list):
    list_of_lists = []
    for split in range(0, len(list), 1):
        list_of_lists.append(list[split:split + 1])

    return list_of_lists


# combinam /merge-uim 2 liste sortate
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


# merge_sort toate perechile de liste din lista de liste doua cate doua
def merge_sort(list_of_lists):
    list_of_merged_lists = []
    for merge_index in range(0, len(list_of_lists), 2):
        if merge_index + 1 < len(list_of_lists):
            list_of_merged_lists.append(merge(list_of_lists[merge_index], list_of_lists[merge_index + 1]))
        else:  # cazul in care ramane o lista nepereche
            list_of_merged_lists.append(list_of_lists[merge_index])
    return list_of_merged_lists


list = [12, 2, 3, 4, 5, 7, 9, 30, 21, 99, 1]
print(f"Initial list: {list}")
list_of_lists = split(list)
print(f"Splited list: {list_of_lists}")

list_of_merged_lists = []
n = len(list)  # log de lungimea listei ne ajuta la numarul de pasi de merge
for i in range(int(math.log(n, 2) + 1)):
    list_of_merged_lists = merge_sort(list_of_lists)
    print(list_of_merged_lists)
    list_of_lists = list_of_merged_lists

print(f"Sorted list: {list_of_lists[0]}")

