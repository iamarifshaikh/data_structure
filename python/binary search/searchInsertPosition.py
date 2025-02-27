def search_insert_position():
    array = [1, 3, 5, 6]
    target = int(input("Enter the target number: "))
    lower = 0
    higher = len(array) - 1
    
    while lower <= higher:
        middle = (lower + higher) // 2
        
        if array[middle] == target:
            return middle
        
        elif array[middle] > target:
            higher = middle - 1

        elif array[middle] < target:
            lower = middle + 1            
    
    return lower

search_insert_position()