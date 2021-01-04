def linear_search(array, item):
    for a in array:
        print(a)
        if a == item:
            return True


if __name__ == '__main__':
    myArray = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    myItem = 44
    position = linear_search(myArray, myItem)
    print(f"{myItem} exista in lista: {position}")
