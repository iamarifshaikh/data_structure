def selectionSort(array):
    
    length = len(array)

    for i in range(length):
        minimum_index = i

        for j in range(i+1,length):
            if array[j] < array[minimum_index]:
                minimum_index = j
        #  Swapping The Values By Creating A Temporary Variable
        temp = array[i]
        array[i] = array[minimum_index]
        array[minimum_index] = temp

        # Swapping The Values By Creating The Tuples
        # (array[i], array[minimum_index]) = (array[minimum_index], array[i])
    

if __name__ == "__main__":
    print("Before Sorting: ")
    array = [24,35,82,-3,-9,14]
    print(array)
    selectionSort(array)
    print("After Sorting: ")
    print(array)