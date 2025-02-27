def removeDuplicates():
    array = [1,1,1,1,2,2,3,3,4,4,5,5,5,5,6,6,7,7]
    
    if not array:
        return 0 

    i = 0
    
    for j in range(1,len(array)):
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]
            print(array)            
    return i + 1

if __name__ == '__main__':
    removeDuplicates()