def lowerBound():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    length = len(array)
    low = 0
    high = length - 1
    answer = length
    target = 7
    
    while low < high:
        mid = (low + high) // 2
        if array[mid] < target:
            answer = array[mid]
            low = mid + 1
        else:
            high = mid        
    print(answer)
if __name__ == '__main__':
    lowerBound()
