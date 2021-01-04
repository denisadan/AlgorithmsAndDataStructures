list_string = ["ae", "io", "ae", "ou", "dddedede"]
list_int = [1, 2, 3, 44, 4, 4, 5]


################################################################
def remove_duplicates(listofElements):
    uniqueList = []
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    return uniqueList


# sau
# listOfNums = list(set(listOfNums))

################################################################
# Check if all elements in list are None
def check_if_all_none(list_of_elem):
    result = True
    for elem in list_of_elem:
        if elem is not None:
            return False
    return result


################################################################

# Check if all elements in list are the same and match the given item
def check_if_all_same(list_of_elem, item):
    result = True
    for elem in list_of_elem:
        if elem != item:
            return False
    return result


################################################################

# if 'ae' in list_string: print("yes")
# if 4 in list_int: print("yes")
# complexity O(1)
def check_duplicates(list_int):
    list_as_set = set(list_int)
    if len(list_int) == len(list_as_set):
        print("no duplicates")
    else:
        print(f"we have duplicates.\n {list_int} \n {list_as_set}")


check_duplicates(list_int)


################################################################

# complexity O(n)
def check_duplicates_with_frequency(list_int):
    # key: nr
    # value: freq
    # [1:1, 2:1, 4:2]
    dict_of_freq = dict()
    for element in list_int:
        if element in dict_of_freq:
            dict_of_freq[element] += 1
        else:
            dict_of_freq[element] = 1
    print(f"{dict_of_freq}")
    return dict_of_freq


check_duplicates_with_frequency(list_int)


################################################################
def get_duplicates_with_info(list_int):
    dict_of_elems = dict()
    index = 0
    for elem in list_int:
        if elem in dict_of_elems:
            dict_of_elems[elem][0] += 1
            dict_of_elems[elem][1].append(index)
        else:
            dict_of_elems[elem] = [1, [index]]
        index += 1

    dict_of_elems = {key: value for key, value in dict_of_elems.items() if value[0] > 1}
    return dict_of_elems


array = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'algorithms', 'test']
dictionary = get_duplicates_with_info(array)
for key, value in dictionary.items():
    print(key, ' :: ', value)
################################################################
