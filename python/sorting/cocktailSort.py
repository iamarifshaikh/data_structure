def cocktailSort(array):
    length = len(array)
    swapped = True
    start = 0
    end = length - 1

    while swapped:
        # Reset swapped to false to check if any swaps happen in this pass
        swapped = False

        # Forward Pass: Left To Right
        for i in range(start, end):
            if array[i] > array[i+1]:
                temporary = array[i]
                array[i] = array[i+1]
                array[i+1] = temporary
                swapped = True  
        
        # If no swaps in forward pass, the array is sorted
        if not swapped:
            print("Array is already sorted")
            break
        
        # Move end pointer one step back since the largest element is in place
        end -= 1

        # Reset swapped to false for the backward pass incase if theres any swapping needs 
        swapped = False

        # Backward Pass: From Right To Left
        for j in range(end - 1, start - 1, -1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
                swapped = True

        # Move the "start" pointer one step forward as the smallest element is in place
        start +=1

if __name__ == '__main__':
    array = [24,35,82,-3,-9,14,10]
    print("Before Sorting: ")
    print(array)
    cocktailSort(array)
    print("After Sorting: ")
    print(array)