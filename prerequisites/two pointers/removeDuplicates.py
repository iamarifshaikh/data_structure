def removeDuplicates(array):
    if not array:
        return 0
    
    unique_index = 0
    
    for i in range(len(array)):
        if array[i] != array[unique_index]:
            unique_index += 1
            array[unique_index] = array[i]
    return unique_index + 1