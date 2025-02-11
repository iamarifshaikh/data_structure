def removeElement():
    array = [1,2,3,4,5,6,3,3]
    k = 0
    value = 1
    for x in range(len(array)):
        if array[x] != value:
            array[k] = array[x]
            print(array)
            k += 1
    print(f"New Length of an array is ", k)
    print(f"Array after modification: ",array)
    return k

if __name__ == '__main__':
    removeElement()