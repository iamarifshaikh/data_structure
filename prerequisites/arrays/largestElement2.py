def largestElement(length,array):

    max = array[0]
    
    for i in range(length):
        if array[i] > max:
            max = array[i]
            
    return max
        
if __name__ == '__main__':
    array = [50,12,43,12,67,8,3,88]
    length = len(array)
    max = largestElement(length,array)
    print("The largest element in the array is " + str(max))