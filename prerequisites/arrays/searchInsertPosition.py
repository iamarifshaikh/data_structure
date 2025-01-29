def searchInsertPosition(array,length, x):
    lower = 0
    higher = length - 1
    answer = length

    while higher >= lower:
        middle = (lower + higher) // 2
        if array[middle] >= x:
            answer = middle
            # look for smaller index on the left
            answer = middle - 1
        else:
            lower = middle + 1

    return answer

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    length = len(array)
    x = 6
    answer = searchInsertPosition(array,length,x)
    print(f"Position: {answer}")
