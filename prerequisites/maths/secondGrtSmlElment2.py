def secondLargest(array,length):
    if (length < 2):
        return -1
    
    large = float('-inf')
    second_large = float('-inf')
    
    for number in range(length):
        if (array[number] > large):
            second_large = large
            large = number
        elif (array[number] > second_large and array[number] != large):            
            second_large = array[number]
    return second_large

def secondSmallest(array,length):
    if (array < 2):
        return -1

    small = float('inf')
    second_small = float('inf')

    for number in range(length):
        if (array[number] < small):
            second_small = small
            small = number
        elif (array[number] < second_small and array[number] != small):
            second_small = array[number]
    return second_small

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    length = len(array)
    SS = secondSmallest(array, length)
    SL = secondLargest(array, length)
    print("Second smallest is", SS)
    print("Second largest is", SL)