def moveZerosToEnd(array):
    # Step 1: Copy non-zeros elements from original array to temporary array
    temp = []

    n = len(array)

    for i in range(n):
        if array[i]!=0:
            temp.append(array[i])

    # Number of non-zeros elements
    non_zero = len(temp)

    # Step 2:Copy elements from temp to fill first non-zeros fields of original array

    for i in range(non_zero):
        array[i] = temp[i]

    # Step 3: Fill remaining non-zeros fields of original array
    for i in range(non_zero, n):
        array[i] = 0

    return array

if __name__ == '__main__':
    array = [0,0,4,2,3,7,0,5,1,8]
    moveZerosToEnd(array)
    print(array)