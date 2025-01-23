def insertionSort(array):    
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key

if __name__ == '__main__':
    array = [10,5,11,3,1,-5,12,1,4]
    insertionSort(array=list)