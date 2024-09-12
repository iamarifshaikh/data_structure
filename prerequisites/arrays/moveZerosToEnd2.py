def printArray(length,array):
    for i in range(length):
        print(array[i], end=" ")
    print()

def moveZeros(length,array):
    j = -1

    for i in range(length):
        if array[i] == 0:
            j = i
            break

    if j == -1:
        return array

    for i in range(j + 1, length):  # Start from the next element after the first zero
        if array[i] != 0:
            array[i], array[j] = array[j], array[i]  # Swap zero with non-zero element
            j += 1  # Move the zero pointer to the next position

    return array

if __name__ == "__main__":
    array = [0,0,3,5,6,7,10,0,0,1]
    length = len(array)
    print("The following are the contents of the array before moving zeros: ")
    printArray(length,array)
    
    moveZeros(length,array)
    
    print("The following are the contents of the array after moving zeros: ")
    printArray(length,array)
