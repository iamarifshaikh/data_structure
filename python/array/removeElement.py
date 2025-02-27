def removeElement():
    array = [0, 1, 2, 2, 3, 0, 4, 2]
    k = 0
    value = 1
    for x in range(len(array)):
        if array[x] != value:
            array[k] = x
            print(array)
            k += 1
    print(f"New Length of an array is ", k)
    print(f"Array after modification: ",array)
    return k

if __name__ == '__main__':
    removeElement()
