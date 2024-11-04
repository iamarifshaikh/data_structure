# def bubbleSort(array):
#     length = len(array)

#     for i in range(length):
#         # Keep Tracking Of Swapping
#         swapped = False

#         # Loop to compare array elements
#         for j in range(0, length - i - 1):

#             if array[j] > array[j+1]:
#                 # Swapping Using temporary variable
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp

#                 # Swapping Using Simultaneous Assignment
#                 # (array[j], array[j+1]) = (array[j+1],array[j])
#             swapped = True
    
#         if not swapped:
#             break

def bubbleSort(array):
    length = len(array)
    swapped = True # Start with swapped as True to enter the loop

    while swapped:
        swapped = False

        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True # Set swapped to True to indicate a swap occurred

        length -= 1  # Reduce the range by one since the last element is sorted

if __name__ == "__main__":
    array = [24,35,82,-3,-9,14]
    print("Before Sorting: ")
    print(array)
    bubbleSort(array)
    print("After Sorting: ")
    print(array)
