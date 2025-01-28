def left_rotate_naive(array,length,k):
    # Scenario 1: If k <= n, rotating k times will move elements correctly without any issues
    # Scenario 2: If k >= n, rotating k times will the array returns to its original state after n rotations. 
    # Any extra rorations beyond n are equivalent to just k % n rotations.    
    
    k = k % length 
    for _ in range(k):
        first = array.pop(0) # Remove the first element
        array.append(first) # And add it to the end
    for j in range(length):
        print(array[j], end=" ")
        
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,]
    length = len(array)
    k = 9
    
    left_rotate_naive(array,length,k)
    