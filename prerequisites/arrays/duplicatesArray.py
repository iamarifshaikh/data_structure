def remove_duplicates_array(array,length):
    unique = set()

    for i in range(length):
        unique.add(array[i])

    k = len(unique)
    j = 0  # This is used to overwrite the array in-place
    
    for x in unique:
        array[j] = x  # Assign unique values to array
        j += 1  # Move index forward
    
    return k 

if __name__ == '__main__':
    array = [1,1,2,3,2,4,5,6,7,8,4,3]
    length = len(array) 
    result = remove_duplicates_array(array,length)
    for i in range(result):
        print(array[i],end=" ")
