def bubbleSort(array):
    length = len(array)

    for i in range(length):
        # Keep Tracking Of Swapping
        swapped = False

        # Loop to compare array elements
        for j in range(0, length - i - 1):

            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

            swapped = True
    
        if not swapped:
            break

if __name__ == "__main__":
    array = [24,35,82,-3,-9,14]
    print("Before Sorting: ")
    print(array)
    bubbleSort(array)
    print("After Sorting: ")
    print(array)
