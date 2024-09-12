def upperBound(x,length, number):
    low = 0
    high = length - 1
    answer = length
    
    while low <= high:
        middle = (low + high) // 2
        
        if array[middle] >= x:
            answer = array[middle]
            high = middle - 1
            
        elif array[middle] <= x:
            low = middle + 1
    
    return answer

if __name__ == '__main__':
    array = [1, 3, 5, 7, 9]
    x = 6
    length = len(array)
    index = upperBound(x, length, array)
    print("The upper bound is the index:", index)