def right_rotate_naive(array,length,k):
    k = k % length
    for _ in range(k):
        last = array.pop() # Remove the last element
        array.insert(0,last)
    for j in range(length):
        print(array[j], end=" ")

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9,10]
    length = len(array)
    k = 2
    
    right_rotate_naive(array,length,k)